from commands import education

commands = ["chromium", "constant", "element", "help", "news", "rate", "reddit", "subscribe", "urban", "weather", "xkcd"]

help = (
"""
# Help

Commands:
    - chromium
    - constant
    - element
    - help
    - news
    - rate
    - reddit
    - subscribe
    - urban
    - weather
    - xkcd

Use !help <command\> to get more information about a command.
"""
)

help_text = (
"""
# Chromium 

Returns the latest stable Chromium version.

Arguments: None

Usage: !chromium
""",
f"""
# Constant

Returns the value of the required scientific or mathematical constant.

List of available constants:
{list(education.values)}

Arguments:
    - const_name

Usage: !constant <name\>
""",
"""
# Element (Chemistry)

Returns information about a given element.

Arguments:
    - element_name

Usage: !element <name\>
""",
"""
Why would you need help with the help command?
""",
"""
# News

Enlightens you with news from around the world.

Arguments: 
    - tech 
    - politics
    - onion

Usage: !news <arguments\>
""",
"""
# Rate 

Rates you based on a category

Arguments:
    - category

Usage: !rate <category\>
""",
"""
# Reddit

Get shitty Reddit memes directly in Matrix.

Arguments:
    - subreddit
""",
"""
# Subscribe 

Subscribe to any RSS feed (including YouTube channels).
Currently only supports YouTube.

Arguments:
    - platform
    - ID

Usage: !subscribe <platform> <ID>

Example: !subscribe youtube UCuAXFkgsw1L7xaCfnd5JJOw
""",
"""
# Urban Dictionary

Get the definition of a word using Urban Dictionary.

Arguments: 
    - word
    - definition rank (optional)

Usage: !urban <word\> | <definition rank\>
""",
"""
# Weather

Gives you today's weather report.

Arguments: None

Usage: !weather
""",
"""
# XKCD

Read XKCD comics directly in Matrix

Arguments:
    - latest
    - random

Usage: !xkcd <argument\> or !xkcd <comic number\>
"""
)

dev_help = (
f"""
# Developer commands help

shell:
    - Super dangerous command that basically gives you a limited root shell from Matrix.
    - Use wisely
    - Add your command after `shell`

temp/temperature:
    - Returns the current SoC temperature
    - No extra arguments

uptime: 
    - Returns system uptime
    - No extra arguments

update:
    - Returns a list of system updates
    - No extra arguments

upgrade:
    - Performs a system upgrade
"""
)