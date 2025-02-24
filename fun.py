"""
✘ Commands Available

• `{i}joke`
    To get joke.

• `{i}url <long url>`
    To get a shorten link of long link.

• `{i}decide`
    Decide something.

• `{i}gif <your query>`
    Sends the desired gif related to your query.

• `{i}vtog <in reply to a video>`
    Converts any video to a gif with low time limit(takes time).

• `{i}xo`
    Opens tic tac game only where using inline mode is allowed.

• `{i}wordi`
    Opens word game only where using inline mode is allowed.

• `{i}gps <name of place>`
    Shows the desired place in the map.

"""

import os
from pyjokes import get_joke
import requests
import random
from . import *
from telethon.errors import ChatSendMediaForbiddenError
from telethon.errors.rpcerrorlist import ChatSendGifsForbiddenError
import moviepy.editor as m


@ultroid_cmd(pattern="joke$")
async def _(ult):
    await eor(ult, get_joke())


@ultroid_cmd(pattern="url ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        await eor(event, "Give some url")
        return
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await eor(event,
                  "Shortened url==> {} for the given url==> {}.".format(
                      response_api,
                      input_str)
                  )
    else:
        await eor(event, "`Something went wrong. Please try again Later.`")


@ultroid_cmd(pattern="decide$")
async def _(event):
    hm = await eor(event, "`Deciding`")
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    r = requests.get("https://yesno.wtf/api").json()
    try:
        await ultroid_bot.send_message(
            event.chat_id,
            r["answer"],
            reply_to=message_id,
            file=r["image"])
        await hm.delete()
    except ChatSendMediaForbiddenError:
        await eor(event, r['answer'])


@ultroid_cmd(pattern="gif ?(.*)")
async def gifs(ult):
    get = ult.pattern_match.group(1)
    if not get:
        return await eor(ult, "`.gif <query>`")
    m = await eor(ult, "`Searching gif ...`")
    gifs = await ultroid_bot.inline_query("gif", f"{get}")
    try:
        await gifs[0].click(ult.chat.id,
                        reply_to=ult.reply_to_msg_id,
                        silent=True,
                        hide_via=True)
        await m.delete()
    except ChatSendGifsForbiddenError:
        await m.edit("`Sending Gif is Restricted in this Chat !!`")


@ultroid_cmd(pattern="vtog$")
async def vtog(ult):
    reply = await ult.get_reply_message()
    if reply is None:
        return await ult.edit("`Reply to any Video`")
    xx = await eor(ult, "`Processing Takes Time...`")
    lol = await ultroid_bot.download_media(reply.media)
    file_name = "ultroid.gif"
    clip = (m.VideoFileClip(lol).subclip((4.3), (5.8)).resize(0.3))
    clip.write_gif(file_name)
    await ultroid_bot.send_file(
        ult.chat_id,
        file_name,
        reply_to=ult.reply_to_msg_id
        )
    os.remove(lol)
    os.remove(file_name)
    await xx.delete()


@ultroid_cmd(pattern="xo$")
async def xo(ult):
    xox = await ultroid_bot.inline_query("xobot", "play")
    await xox[random.randrange(0, len(xox)-1)].click(
        ult.chat.id,
        reply_to=ult.reply_to_msg_id,
        silent=True,
        hide_via=True
        )
    await ult.delete()


@ultroid_cmd(pattern="wordi$")
async def word(ult):
    game = await ultroid_bot.inline_query("wordibot", "play")
    await game[0].click(ult.chat.id,
                        reply_to=ult.reply_to_msg_id,
                        silent=True,
                        hide_via=True)
    await ult.delete()


@ultroid_cmd(pattern="gps (.*)")
async def map(ult):
    get = ult.pattern_match.group(1)
    if not get:
        return await eor(ult, "Use this command as `.gps <query>`")
    gps = await ultroid_bot.inline_query("openmap_bot", f"{get}")
    await gps[0].click(
        ult.chat.id,
        reply_to=ult.reply_to_msg_id,
        silent=True,
        hide_via=True)
    await ult.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
