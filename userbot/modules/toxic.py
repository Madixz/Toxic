from userbot import CMD_HELP, bot
from telethon import events
import asyncio


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "sinick1":

        await event.edit(input_str)

        animation_chars = [
            "`Sayang Pengen🥺` ",
            " Udah Kebelet ",
            " Pengen Ngewe ",
            " Ayangg Ayokkk ",
            " Ngeweee ",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "sinick2":

        await event.edit(input_str)

        animation_chars = [
            "`Masih Teringat` ",
            " Di Malam Itu Kita Bercumbu",
            " Di Bawah Sinar Rembulan ",
            " Engkau MencumbuiKu ",
            " Dengan Sangat Ganas ",
            " Kau Isap Kontol Ku ",
            " Dan Ku Jilat Memek Mu ",
            " Skip Nanti Lu Sange",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "sinick3":

        await event.edit(input_str)

        animation_chars = [
            "`Teruntuk Kamu` ",
            " Hay Cantik, Sudah Lama ",
            " Perasaan Ini Ku SembunyiKan ",
            " Tapi Sekarang ",
            " Aku Tak Dapat Menampung Semuanya ",
            " Semakin Aku Diam, Semakin Aku Gelisah ",
            " Hati Ini Menginginkan Dirimu ",
            " Mau Kah Kamu Menjadi PendampingKu?",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 7

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "sinick4":

        await event.edit(input_str)

        animation_chars = [
            "`Connecting To Hacked Private Server...`",
            "`Target Selected.`",
            "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Looking for telegram data...`\nETA: 0m, 20s",
            "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Found folder sd/telegram...`\n`Looking for telegram data : ✅`\nETA: 0m, 10s",
            "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Searching for databases....`\n`Looking for telegram data : ✅`\n`Found folder sd/telegram : ✅ `\nETA: 0m, 15s",    
            "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`\n`Found msgstore.db.crypt12...`\n`Looking for telegram data : ✅`\n`Found folder sd/telegram : ✅ `\n`Searching for databases : ✅ `\nETA: 0m, 09s",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Trying to Decrypt...`\n`Looking for telegram data : ✅`\n`Found folder sd/telegram : ✅\n`Searching for databases : ✅`\n`Found msgstore.db.crypt12 :  ✅`\n`⚠️ error occurred ..`\nETA: 0m, 25s",
            "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `\n`Decryption successful!`\n`Looking for telegram data : ✅`\n`⚠️ error occurred ..`\n`Found folder sd/telegram : ✅`\n`⚠️ error occurred ..`\n`Searching for databases : ✅`\n`Found msgstore.db.crypt12 :  ✅`\nETA: 0m, 25s",
            "`Hacking... 84%\n█████████████████████▒▒▒▒ `\n`Scanning file...`\n`Looking for telegram data : ✅`\n`⚠️ error occurred ..`\n`Found folder sd/telegram : ✅`\n`⚠️ error occurred ..`\n`⚠️ error occurred ..`\n`Searching for databases : ✅`\n`Found msgstore.db.crypt12 :  ✅`\n`Scanning file :  ✅`\nETA: 0m, 16s",
            "`Hacking... 100%\n` 98% HACKED`",
            "`Targeted Account Hacked...`\n\n`_______________________`\n`result ... :)`\n\n`Chatlist : ✅`\n`Calls : ✅`\n`groups : ✅`\n `Contacts : ✅`\n`Channel : ✅`\n`Deleted Messages : ❌`\n`Edited Messages : ❌`\n`All API Tokens : ✅`\n\n`Pay 99999$ to my boss.... `Or send your girlfriend's number To Remove This Hack`"
         ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


CMD_HELP.update({
    "toxic":
    "`.sinick1`\
    \nUsage: pengen.\
    \n\n`.sinick2`\
    \nUsage: sange."
})
