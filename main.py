import matrix as botlib
from commands import *

creds = botlib.Creds(base.get_homeserver(), base.get_username(), base.get_password())
PREFIX = '!'
bot = botlib.Bot(creds)

@bot.listener.on_message_event
async def chromium(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("chromium", case_sensitive=False):
        await bot.api.send_text_message(room.room_id, f"The latest Chromium version is {base.get_chromium()}")

@bot.listener.on_message_event
async def element(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("element", case_sensitive=False):
        arg = match.args()
        if arg[0]:
            info = education.get_element(str(arg[0]))
            if info == "error":
                await bot.api.send_text_message(room.room_id, f"Are you dumb, that element does not exist {message.source['sender']}")
            else:
                message = (
f"""
Name: {info[6]}
Symbol: {info[1]}
Number: {info[0]}
Mass: {info[4]}
Type: {info[5]}
Located at Period {info[2]} and Group {info[3]} in the Periodic Table. 
"""
                )
                await bot.api.send_markdown_message(room.room_id, message)
        else:
            await bot.api.send_markdown_message(room.room_id, "Insufficient arguments provided, please give provide an element.")

@bot.listener.on_message_event
async def constant(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("constant", case_sensitive=False):
        if match.args():
            if match.args()[0]:
                char = education.constant(match.args()[0])
                if char != "error":
                    await bot.api.send_markdown_message(room.room_id, char)
                else:
                    resp = (
                        "Don't have that constant yet.\n"
                        "Here is a list of the available constants:\n"
                        f"{list(education.values)}"
                    )
                    await bot.api.send_markdown_message(room.room_id, resp)
        else:
            await bot.api.send_markdown_message(room.room_id, "Invalid inputs given for that command.")

@bot.listener.on_message_event
async def help(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("help", case_sensitive=False):
        arg = match.args()
        if arg:
            await bot.api.send_markdown_message(room.room_id, base.send_help(arg[0]))
        else:
            await bot.api.send_markdown_message(room.room_id, base.send_help(None))

@bot.listener.on_message_event
async def xkcd(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("xkcd", case_sensitive=False):
        arg = match.args()
        if arg:
            if str(arg[0]).isdigit():
                if comic.number(arg[0]) != "OK":
                    await bot.api.send_text_message(room.room_id, "Invalid comic number given")
                    return
                else:
                    await bot.api.send_image_message(image_filepath="assets/temp.jpg", room_id=room.room_id)
                    await bot.api.send_text_message(room.room_id, "Explanation: " + comic.explain())
                    return
            if (arg[0] != "random") and (arg[0] != "latest"):
                await bot.api.send_markdown_message(room.room_id, "Invalid arguments given")
            if arg[0] == "random":
                altText = comic.random()
                await bot.api.send_image_message(image_filepath="assets/temp.jpg", room_id=room.room_id)
                await bot.api.send_text_message(room.room_id, altText)
                await bot.api.send_text_message(room.room_id, "Explanation: " + comic.explain())
            if arg[0] == "latest":
                altText = comic.latest()
                await bot.api.send_image_message(image_filepath="assets/temp.jpg", room_id=room.room_id)
                await bot.api.send_text_message(room.room_id, altText)
                await bot.api.send_text_message(room.room_id, "Explanation: " + comic.explain())
        else:
            altText = comic.random()
            await bot.api.send_image_message(image_filepath="assets/temp.jpg", room_id=room.room_id)
            await bot.api.send_text_message(room.room_id, altText)
            await bot.api.send_text_message(room.room_id, "Explanation: " + comic.explain())

@bot.listener.on_message_event
async def ud(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("urban", case_sensitive=False):
        arg = match.args()
        if arg:
            word = ''.join(arg)
            if '|' in word:
                args = word.split('|')
                try:
                    resp = urban.definition(args[0], int(args[1]))
                except:
                    resp = "Invalid input given."
                await bot.api.send_markdown_message(room.room_id, resp)
            else:
                word = ' '.join(arg)
                resp = urban.definition(word)
                await bot.api.send_markdown_message(room.room_id, resp)
        else:
            await bot.api.send_text_message(room.room_id, "No word given.")

@bot.listener.on_message_event
async def news(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("news", case_sensitive=False):
        if match.args():
            if match.args()[0] == "tech":
                await bot.api.send_markdown_message(room.room_id, feed.any_reddit("technology"))
            elif match.args()[0] == "politics":
                await bot.api.send_markdown_message(room.room_id, feed.any_reddit("politics"))
            elif match.args()[0] == "onion":
                await bot.api.send_markdown_message(room.room_id, feed.any_reddit("nottheonion"))
            else:
                await bot.api.send_text_message(room.room_id, "Don't have that category of news.")
        else:
            await bot.api.send_markdown_message(room.room_id, feed.any_reddit("worldnews"))

@bot.listener.on_message_event
async def reddit(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("reddit", case_sensitive=False):
        arg = match.args()
        if arg:
            try:
                if arg[0] == "image":
                    if meme.validate(arg[1]):
                        post = meme.subreddit(arg[1])
                        await bot.api.send_markdown_message(room.room_id, post[0])
                        await bot.api.send_image_message(image_filepath="assets/meme.jpg", room_id=room.room_id)
                        await bot.api.send_markdown_message(room.room_id, post[1])
                    else:
                        await bot.api.send_text_message(room.room_id, "This subreddit either does not exist is not whitelisted for access.")
                elif arg[0] == "text":
                    await bot.api.send_markdown_message(room.room_id, feed.any_reddit(arg[1]))
                else:
                    await bot.api.send_text_message(room.room_id, "Invalid syntax.")
            except IndexError:
                await bot.api.send_text_message(room.room_id, "Invalid syntax.")           
        else:
            post = meme.random()
            await bot.api.send_markdown_message(room.room_id, post[0])
            await bot.api.send_image_message(image_filepath="assets/meme.jpg", room_id=room.room_id)
            await bot.api.send_markdown_message(room.room_id, post[1])

@bot.listener.on_message_event
async def dev(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("dev", case_sensitive=False):
        if message.source['sender'] == f"@{base.get_owner()}:{base.get_homeserver().replace('https://', '')}":
            try:
                if match.args()[0] == "shell":
                    no_no_list = ["rm", "rmdir", "python", "bash", "sh", "reboot", "shutdown", "poweroff", "docker", "clear", "systemctl", "wipefs", "fdisk"]
                    if len(list(set(match.args()[1:]).intersection(no_no_list))) == 0:
                        info = base.shell(' '.join(match.args()[1:])).split('\n')
                        msg = (
f"""
    {f"{chr(10)}    ".join(str(x) for x in info)}                       
"""
                        )
                        await bot.api.send_markdown_message(room.room_id, msg)
                    else:
                        await bot.api.send_html_message(room.room_id, "<h1>Action Prohibited</h1>")
                if match.args()[0] == "temp" or match.args()[0] == "temperature":
                    await bot.api.send_text_message(room.room_id, "SoC temperature is " + base.get_temperature())
                if match.args()[0] == "uptime":
                    await bot.api.send_text_message(room.room_id, base.get_uptime())
                if match.args()[0] == "update":
                    from scheduler import update_report
                    await bot.api.send_markdown_message(room.room_id, update_report.sys_update_reporter())
            except IndexError:
                await bot.api.send_markdown_message(room.room_id, base.send_dev_help())
        else:
            await bot.api.send_markdown_message(room.room_id, "This command is obviously developer only.")

@bot.listener.on_message_event
async def rate(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("rate", case_sensitive=False):
        if match.args():
            category = ' '.join(match.args())
            await bot.api.send_text_message(room.room_id, f"You are {base.rate()}% {category}")
        else:
            await bot.api.send_text_message(room.room_id, "No category given to rate.")

@bot.listener.on_message_event
async def privacy(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    a = message.source['content']['body']
    if match.is_not_from_this_bot() and "https://" in a and "matrix.to" not in a:
        await bot.api.send_text_message(room.room_id, base.privacy_filter(a))

@bot.listener.on_message_event
async def weather(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("weather", case_sensitive=False):
        await bot.api.send_html_message(room.room_id, weather_report.weatherData())

@bot.listener.on_message_event
async def subscribe(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("subscribe", case_sensitive=False):
        args = match.args()
        if args:
            try:
                if args[0] == "youtube":
                    await bot.api.send_text_message(room.room_id, feed.yt_subscribe(args[1], message.source['sender']))
                else:
                    raise IndexError('')
            except IndexError:
                await bot.api.send_markdown_message(room.room_id, "Invalid arguments given. Use `!help subscribe`")
        else:
            await bot.api.send_markdown_message(room.room_id, "Invalid arguments given. Use `!help subscribe`")

@bot.listener.on_message_event
async def garfield(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("garfield", case_sensitive=False):
        info = comic.get_garfield()
        await bot.api.send_image_message(room.room_id, info[0])
        await bot.api.send_text_message(room.room_id, f"Release Date: {info[1]}/{info[2]}/{info[3]}")

bot.run()
