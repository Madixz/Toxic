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



@register(outgoing=True, pattern="^.CHB$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        f"❇ ** Ch Bokep :** [ Bokep ](https://t.me/joinchat/VYezAmeu_YM5NTQ9)\n"
        f"❇ **     :** [-]( )\n"
        f"❇ **     :** [-]( )\n"
    )


@register(outgoing=True, pattern="^.CHB$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        f"⚜️ ┗┓ ** R U L E S ** ┏┛ ⚜️ \n\n"
        f"** ✥ Wajib Follow Ig Di Bawah **\n\n"
        f"** ✥ Jika sudah follow ig di bawah bisa langsung pc/dm(jika tidak memilili tele) ke akun yang bersangkutan untuk follow back. **\n\n"
        f"** ✥ Jika dalam kurun waktu 1 hari tidak difollow back bisa melaporkan ke admin dan anda bisa unfoll ig bersangkutan. **\n\n"
        f"** ✥ Jika mau mendaftar agar ig nya ada didaftar ig bisa pc ke [ Admin ]( https://t.me/Bot_Sinick ) **\n\n"
        f"⚜️ ┗┓ ** DAFTAR IG ** ┏┛ ⚜️ \n\n"
        f"❇ ** Bot_Sinick :** [ Ig ](https://instagram.com/bot_sinick?igshid=16p9mzk9kne8v) [ Tele ]( https://t.me/Bot_Sinick ) \n"
        f"❇ ** Jess       :** [ Ig ]( https://instagram.com/jeve_jess?igshid=a36x6yczxix6 ) \n"
        f"❇ ** Ayu        :** [ Ig ]( https://instagram.com/_ayy614?igshid=pzm0rejkawtz )\n"
    )




CMD_HELP.update({
    "jngn buka nnti eror":
    "`.okp`\
\nUsage: Jangan di coba kalo tidak mau eror.\
\n\n`.okp2`\
\nUsage: Jangan di coba kalo tidak mau eror.\
\n\n`.okp3`\
\nUsage: Jangan di coba kalo tidak mau eror.\
\n\n`.viral`\
\nUsage: Jangan di coba kalo tidak mau eror."
})
