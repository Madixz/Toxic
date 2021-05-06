""" Userbot module for other small commands. """

from random import randint
from time import sleep
from os import execl
import asyncio
import sys
import os
import io
import sys
from userbot import ALIVE_NAME, BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register
from userbot.utils import time_formatter
import urllib
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

opener = urllib.request.build_opener()
useragent = 'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36'
opener.addheaders = [('User-agent', useragent)]



@register(outgoing=True, pattern="^.bkp$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        f"✦҈͜͡➳ ** Ch Bokep :** [ GudangBocep ](https://t.me/joinchat/VYezAmeu_YM5NTQ9)\n"
        f"✦҈͜͡➳ **     :** [-]( )\n"
        f"✦҈͜͡➳ **     :** [-]( )\n"
    )


@register(outgoing=True, pattern="^.ig$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        f"✦҈͜͡➳ ** Link Mutualan Ig :** [ Daftar Ig ](https://telegra.ph/Daftar-Ig-05-01-2)\n"
        f"✦҈͜͡➳ **     :** [-]( )\n"
        f"✦҈͜͡➳ **     :** [-]( )\n"
    )



