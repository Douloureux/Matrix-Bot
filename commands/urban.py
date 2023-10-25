from lib import urbandictionary as ud

def definition(phrase, rank=1) -> str:
    try:
        defs = ud.define(phrase)
        retval = (
f"""
# {defs[rank-1].word}

{defs[rank-1].definition}

Examples:
{defs[rank-1].example}
"""
        )
        return retval
    except ValueError:
        return "No definition found"
    except IndexError:
        return "Invalid definition rank given"