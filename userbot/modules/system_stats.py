# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

""" Userbot module for System Stats commands """

import asyncio
import platform
import sys
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version, uname
from shutil import which

import psutil
from telethon import __version__, version

from userbot import (
    ALIVE_EMOJI,
    ALIVE_LOGO,
    ALIVE_NAME,
    ALIVE_TEKS_CUSTOM,
    BOT_VER,
    CMD_HELP,
    UPSTREAM_REPO_BRANCH,
    StartTime,
    bot,
)
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


modules = CMD_HELP


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern=r"^\.(?:alive|on)\s?(.)?")
async def amireallyalive(alive):
    await bot.get_me()
    uptime = await get_readable_time((time.time() - StartTime))
    output = (
        f"╔═════════════╗ \n"
        f"╠ ✥ Master     => `{DEFAULTUSER}` \n"
        f"╠ ✥ Modules   => `{len(modules)} Modules` \n"
        f"╠ ✥ Bot Version     => `{BOT_VER}` \n"
        f"╠ ✥ Python Version     => `{python_version()}` \n"
        f"╠ ✥ Telethon Version   => `{version.__version__}` \n"
        f"╠ ✥ Bot Uptime     => `{uptime}` \n"
        f"╚═════════════╝ \n\n"
        "    **[𝗢𝘄𝗻𝗲𝗿](t.me/Bot_Sinick)**"
    )
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(800)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()



CMD_HELP.update(
    {
        "system": "**Plugin : **`system`.\
        \n\n  •  **Syntax :** `.alive` atau `.on`\
        \n  •  **Function : **Ketik .alive untuk melihat apakah bot Anda berfungsi atau tidak.\
    "
    }
)
