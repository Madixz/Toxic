from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.CHB(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("https://t.me/joinchat/VYezAmeu_YM5NTQ9")


@register(outgoing=True, pattern='^.viral(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("https://drive.google.com/file/d/1GX0OuXdueKUITH1gRGgi_AxNaJ4LsGD9/view?usp=drivesdk")


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
