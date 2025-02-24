# inspired from bin.py which was made by @danish_00
# written by @senku_ishigamiii/@Uzumaki_Naruto_XD

"""
✘ Commands Available -

• `{i}limited`
   Check you are limited or not !

"""

from . import *
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


@ultroid_cmd(pattern="limited$")
async def demn(ult):
    chat = "@SpamBot"
    msg = await eor(ult, "Checking If You Are Limited...")
    async with ultroid_bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=178220800
            )
            )
            await conv.send_message("/start")
            response = await response
            await ultroid_bot.send_read_acknowledge(chat)
        except YouBlockedUserError:
            await msg.edit("Boss! Please Unblock @SpamBot ")
            return
        await msg.edit(f"~ {response.message.message}")



HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
