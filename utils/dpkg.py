# Modified version of https://gist.github.com/yumminhuang/8b1502a49d8b20a6ae70

import apt
import apt_pkg
import os
import sys

SYNAPTIC_PINFILE = "/var/lib/synaptic/preferences"
DISTRO = open("/etc/os-release").readlines()[4].strip().replace("VERSION_CODENAME=", "")

def clean(cache,depcache):
    """ unmark (clean) all changes from the given depcache """
    depcache.init()


def saveDistUpgrade(cache,depcache):
    """ this functions mimics a upgrade but will never remove anything """
    depcache.upgrade(True)
    if depcache.del_count > 0:
        clean(cache,depcache)
    depcache.upgrade()


def get_update_packages():
    """
    Return a list of dict about package updates
    """
    pkgs = []

    apt_pkg.init()
    apt_pkg.config.set("Dir::Cache::pkgcache","")

    try:
        cache = apt_pkg.Cache(apt.progress.base.OpProgress())
    except SystemError as e:
        sys.stderr.write("Error: Opening the cache (%s)" % e)
        sys.exit(-1)

    depcache = apt_pkg.DepCache(cache)
    depcache.read_pinfile()
    if os.path.exists(SYNAPTIC_PINFILE):
        depcache.read_pinfile(SYNAPTIC_PINFILE)
    depcache.init()

    try:
        saveDistUpgrade(cache,depcache)
    except SystemError as e:
        sys.stderr.write("Error: Marking the upgrade (%s)" % e)
        sys.exit(-1)

    for pkg in cache.packages:
        if not (depcache.marked_install(pkg) or depcache.marked_upgrade(pkg)):
            continue
        inst_ver = pkg.current_ver
        cand_ver = depcache.get_candidate_ver(pkg)
        if cand_ver == inst_ver:
            continue
        record = {"name": pkg.name,
                  "security": isSecurityUpgrade(pkg, depcache),
                  "current_version": inst_ver.ver_str if inst_ver else '-',
                  "candidate_version": cand_ver.ver_str  if cand_ver else '-',
                  "priority": cand_ver.priority_str}
        pkgs.append(record)

    return pkgs


def isSecurityUpgrade(pkg, depcache):

    def isSecurityUpgrade_helper(ver):
        """ check if the given version is a security update (or masks one) """
        security_pockets = [("Debian", "%s-updates" % DISTRO)]

        for (file, index) in ver.file_list:
            for origin, archive in security_pockets:
                if (file.archive == archive and file.origin == origin):
                    return True
        return False
    inst_ver = pkg.current_ver
    cand_ver = depcache.get_candidate_ver(pkg)

    if isSecurityUpgrade_helper(cand_ver):
        return True

    for ver in pkg.version_list:
        if (inst_ver and
            apt_pkg.version_compare(ver.ver_str, inst_ver.ver_str) <= 0):
            continue
        if isSecurityUpgrade_helper(ver):
            return True

    return False

def update_avaliable(pkgs):
    if not pkgs:
        return False
    else: 
        return True

def return_updates(pkgs):
    security_updates = list(filter(lambda x: x.get('security'), pkgs))
    text = []
    text.append(f"{len(pkgs)} packages can be updated with {len(security_updates)} security updates.")
    for pkg in pkgs:
        text.append(f"{pkg.get('name')} {'*' if pkg.get('security') else ''}")
    text.append("Packages marked with a * are security updates.")
    return '\n\n'.join(text)

def check_update(pkgs):
    return update_avaliable(pkgs)