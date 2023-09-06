import asyncio

from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator
import random
from FallenRobot import telethn as client

spam_chats = []

EMOJI = [ "🦋",
          "🧚",
          "🥀",
          "🌸",
          "❤️",
          "💓",
          "💐",
          "🍔",
          "🍎",
          "🧋",
          "🍬",
          "🍨",
          "🥪",
          "🫖",
          "🌿",
          "🍁",
          "🌨️",
          "🌷",
          "💮",
          "🧟",
          "🧅",
          "🐷",
          "🦋",
          "🌼",
          "🥩",
          "🍴",
          "🕌",
          "🎉",
          "🪴",
          "🎄",
          "🦅",
          "🦤",
          "🐬",
          "🐔",
          "🦩",
          "🐦",
          "🥪",
          "🥬",
          "🖤",
          "💖",
          "🌺",
          "🍲",
          "🍒",
          "🍷",
          "🍡",
          "🍺",
          "🍦",
          "🍹",
          "🍙",
          "💮",
          "🌧️",
          "💐",
          "🍁",
          "👸",
          "🥦",
          "🐻‍❄️",
          "🐈‍⬛",
          "🌵",
          "🍇",
          "🥃",
          "🏩",
          "🎀",
          "🌴",
          "🎍",
          "🦢",
          "🦆",
          "🐳",
          "🦐",
          "🦑",
          "🕷️",
          "🍨",
          "🧸",
          "🐝",
          "🐣",
          "🍲",
          "🌝",
          "🍷",
          "🍑",
          "🍢",
          "🍡",
          "🍹",
          "🍔",
          "💮",
          "🌧️",
          "🎈",
          "🍁",
          "👸",
          "🥦",
          "🍧",
          "🐈‍⬛",
          "🌵",
          "🦊",
          "🥃",
          "🌴",
          "🎀",
          "🌴",
          "🕊",
          "🦢",
          "🍨",
        ]

FLAGS = [ "🏴",
          "🏴‍☠️",
          "🏁",
          "🚩",
          "🇦🇸",
          "🏳️‍🌈",
          "🏳️‍⚧️",
          "🇺🇳",
          "🇦🇴",
          "🇦🇩",
          "🇩🇿",
          "🇦🇱",
          "🇦🇽",
          "🇦🇫",
          "🇦🇮",
          "🇦🇶",
          "🇦🇬",
          "🇦🇷",
          "🇧🇭",
          "🇧🇸",
          "🇦🇿",
          "🇦🇲",
          "🇦🇺",
          "🇧🇩",
          "🇧🇹",
          "🇧🇴",
          "🇧🇦",
          "🇧🇲",
          "🇧🇯",
          "🇧🇿",
          "🇧🇪",
          "🇧🇼",
          "🇧🇷",
          "🇻🇬",
          "🇧🇳",
          "🇧🇬",
          "🇧🇫",
          "🇧🇮",
          "🇰🇾",
          "🇧🇶",
          "🇨🇻",
          "🇮🇨",
          "🇨🇦",
          "🇨🇲",
          "🇰🇭",
          "🇨🇫",
          "🇹🇩",
          "🇮🇴",
          "🇨🇱",
          "🇨🇳",
          "🇨🇽",
          "🇨🇨",
          "🇨🇮",
          "🇨🇷",
          "🇨🇰",
          "🇨🇩",
          "🇨🇬",
          "🇰🇲",
          "🇨🇴",
          "🇭🇷",
          "🇨🇺",
          "🇨🇼",
          "🇨🇾",
          "🇨🇿",
          "🇩🇰",
          "🇩🇯",
          "🇪🇷",
          "🇬🇶",
          "🇸🇻",
          "🇪🇬",
          "🇪🇨",
          "🇩🇴",
          "🇩🇲",
          "🇪🇪",
          "🇸🇿",
          "🇪🇹",
          "🇪🇺",
          "🇫🇰",
          "🇫🇴",
          "🇫🇯",
          "🇬🇲",
          "🇬🇦",
          "🇹🇫",
          "🇵🇫",
          "🇬🇫",
          "🇫🇷",
          "🇫🇮",
          "🇬🇪",
          "🇩🇪",
          "🇬🇭",
          "🇬🇮",
          "🇬🇷",
          "🇬🇱",
          "🇬🇩",
          "🇬🇾",
          "🇬🇼",
          "🇬🇳",
          "🇬🇬",
          "🇬🇹",
          "🇬🇺",
          "🇬🇵",
          "🇭🇹",
          "🇭🇳",
          "🇭🇰",
          "🇭🇺",
          "🇮🇸",
          "🇮🇳",
          "🇮🇩",
          "🇯🇲",
          "🇮🇹",
          "🇮🇱",
          "🇮🇲",
          "🇮🇪",
          "🇮🇶",
          "🇮🇷",
          "🇯🇵",
          "🎌",
          "🇯🇪",
          "🇯🇴",
          "🇰🇿",
          "🇰🇪",
          "🇰🇮",
          "🇱🇸",
          "🇱🇧",
          "🇱🇻",
          "🇱🇦",
          "🇰🇬",
          "🇰🇼",
          "🇽🇰",
          "🇱🇷",
          "🇱🇾",
          "🇱🇮",
          "🇱🇹",
          "🇱🇺",
          "🇲🇴",
          "🇲🇬",
          "🇲🇶",
          "🇲🇭",
          "🇲🇹",
          "🇲🇱",
          "🇲🇻",
          "🇲🇾",
          "🇲🇼",
          "🇲🇷",
          "🇲🇺",
          "🇾🇹",
          "🇲🇽",
          "🇫🇲",
          "🇲🇩",
          "🇲🇨",
          "🇳🇦",
          "🇲🇲",
          "🇲🇿",
          "🇲🇦",
          "🇲🇸",
          "🇲🇪",
          "🇲🇳",
          "🇳🇷",
          "🇳🇵",
          "🇳🇱",
          "🇳🇨",
          "🇳🇿",
          "🇳🇮",
          "🇳🇪",
          "🇳🇴",
          "🇲🇵",
          "🇲🇰",
          "🇰🇵",
          "🇳🇫",
          "🇳🇺",
          "🇳🇬",
          "🇴🇲",
          "🇵🇰",
          "🇵🇼",
          "🇵🇸",
          "🇵🇾",
          "🇶🇦",
          "🇵🇷",
          "🇵🇹",
          "🇵🇱",
          "🇵🇳",
          "🇵🇭",
          "🇵🇪",
          "🇷🇪",
          "🇷🇴",
          "🇷🇺",
          "🇷🇼",
          "🇼🇸",
          "🇸🇲",
          "🇸🇹",
          "🇸🇽",
          "🇰🇷",
          "🇿🇦",
          "🇸🇬",
          "🇸🇱",
          "🇸🇴",
          "🇸🇧",
          "🇸🇨",
          "🇷🇸",
          "🇬🇸",
          "🇸🇮",
          "🇸🇳",
          "🇸🇦",
          "🇸🇰",
          "🇸🇸",
          "🇪🇸",
          "🇱🇰",
          "🇧🇱",
          "🇸🇭",
          "🇰🇳",
          "🇹🇰",
          "🇹🇬",
          "🇹🇱",
          "🇹🇭",
          "🇬🇧",
          "🇿🇲",
          "🇹🇻",
          "🏴󠁧󠁢󠁷󠁬󠁳󠁿",
          "🇰🇷",
          "🇹🇴",
          "🇻🇳",
          "🇪🇭",
          "🇿🇲",
          "🇺🇿",
          "🇻🇺",
        ]

TAGMES = [ " **holla kaha ho ji ap 🥹🥹** ",
           " **oye buddhu online aao 👉👈** ",
           " **vc join kro baat krte hai babu 😁✨** ",
           " **oii intzaar kar rhi hu aapka 🙁❣️** ",
           " **jane mere jaanemaan bachpan kya pyar mera bhul nhi jana re 🙈🥰** ",
           " **abe on aaja bisi kitna sota hai 🌚👀** ",
           " **sanu ek pal chain na aave sajna tere bina haayee 😅🥀** ",
           " **aur batao kese ho ?? 😌** ",
           " **accha suno to kkrh ap ✨🤍...??** ",
           " **GooD MorninG Jaanemaan 🖼🌸** ",
           " **are vaiyaa aur batao kha chale 👀🤕...!!** ",
           " **tumhri gf vc mie hai jaldi aao 🥴🧸** ",
           " **aal tu jalal tu aaj se mera maal tu 💖🤫** ",
           " **on aa jao bahut miss kar rhi hu aapko 🤗🫶** ",
           " **breakfast hu aapka...??** ",
           " **dinner bana rhe hai hum aapke liya 😊✌️** ",
           " **aapne lunch kia ya nhi...?? 😑😑** ",
           " **beby kaha ho ap..?🤔** ",
           " **tum aaj online nhi dikh rhe theee...?** ",
           " **chalo vc mie song sunte hai aa jao 🤗** ",
           " **yaar sab aa gya ap kaha ho 😇** ",
           " **one plus eight equals to nine , will you be mine 🤭 ??** ",
           " **mele se koi baat nhi krta yha 🥺🥺** ",
           " **are online aa jao na ab too😶** ",
           " **konse class mie ho ap..??🤔** ",
           " **Good Night Beby 🌙🌚** ",
           " **ek kaam krdo na mera 🙂** ",
           " **sad kio ho tum, gf se ladai hui kya 🤧🤧** ",
           " **aapse mil kar accha laga ☺️** ",
           " **suno na buddhu i need vitamin u 👉👈❤️** ",
           " **padhai hui aapki ??😺** ",
           " **kuch to bola na 🥲** ",
           " **are group mie new ladki aayi hai ??😅** ",
           " **aaye haaye sharam gyi kya phone kaati mummi aa gyi kya ?😅** ",
           " **are ruk ruk aati mie 😆😆😆** ",
           " **aur bata bro ladki pati ya abhi bhi mere tarah single hai ??😉** ",
           " **tysm 🙈🙈🙈** ",
           " **do you love me or not ?👀** ",
           " **are tumhre bhaiya kese hai ??🙉** ",
           " **abe tu fir aa gya 😹** ",
           " **chal vc tapak ganna sunte 🫣🫣** ",
           " **insta use krti ho kya tum ??** ",
           " **are beby kaha ho ap 🌝🥀** ",
           " **tumhara breakup hua kya 💔😣 ??** ",
           " **ab hum chalte hai fir milenge 🙃** ",
           " **ole ole gussa kio ho rhe sorry 😊** ",
           " **ab mie bhi ja rhi hu 🧐** ",
           " **chalo mie sone ja rha ohk tata 😁🌷** ",
           " **aur kro dusri ladkiyon se baat good byee 😠** ",
           " **family mie sab kese hai ??❤** ",
           " **kya matter hua re bantai 👱** ",
           " **ab to aaja on tu 🤧❣️** ",
           " **hn hn jao uske pass 😏😏** ",
           " **juth kio bol rha be 🤐** ",
           " **nhi kha lo tum bhi bhav dikhao attitude 😒** ",
           " **ale bhagooo 😮😮** "
           " **hui hui 👀** ",
           " **ek tu cute ek mie cute baki sab darawne bhoot 🙈** ",
           " **mood off ho gya yaar ☹️** ",
           " **kitkat lake do meko 🥺🥺** ",
           " **aaj kuch special hai kya 👀** ",
           " **sab theek thak ?? 🙂** ",
           " **idhar bhi on aa jaya kro ap 🤔** ",
           " **baat to krte nhi aur bol rhe ap mere jaan ho 🥺** ",
           " **haaye kitni masoom hu mie 🦋🐼** ",
           " **aur kal ke tarah mjee kre wapis aj 🤭😅** ",
           " **group mie bhi baat kr liya kro 😕** ",
           " **abe tere bhi gf hai ??👀** ",
           " **ruko ruko mie vi aa rhi gumys 😼** ",
           " **nibbapanti band krde vaii ** ",
           " **aao lovers park chale romance krne ??🙈** ",
           " **enjoy kro ap yaar ☘️🌸** ",
           " **aapki yaad aa rhe hai 🥰** ",
           " **oyeee kidhar chala 🧐** ",
           " **miss you a lot 🥺** ",
           " **mujhe dosti kroge 😊** ",
           " **oo mujhse nalaz hai 🥺🥺** ",
           " **kaha khoye ho ap 😜** ",
           " **babu baad mie aati mie 🥰** ",
           " **abe kya hua tujhe  👱** ",
           " **aur aaj kal kaha rheta be tu ??** ",
           " **hammare liye time nhi auro ke liye hai 😒😒** ",
           " **londiyabaaz kaha hai tu 😂😂** ",
           " **kaha ja rha be kutte 😁❤️** ",
           " **oyee kutti kaha hai tu 🙈🥀** "
           " **aaj pata hai kya hua 🌚😢** ",
           " **yaar mera breakup ho gya 💔😔** ",
           " **uski wajah se tu mood off kio kr rha ** ",
           " **are chor usko kaam krne de uska 👀🥲** ",
           " **tum single ho ya mingle ??** ",
           " **accha ohkie ab to on aajao** ",
           " **are on aaja baandri backchodi kre 😂😁** ",
           " **tere bina accha na lagta beby kaha hai tu ??🥹❤️** ",
           " **uffff kitne hot hu tum sach kahu to insaan nhi bot hu tum 🙈😂** ",
           " **hii handsome kese ho 🤭😅** ",
           " **mujhse bhi baat krlo 😕** ",
           " **dusri gf mil gyi kya tujhe itna busy rheta ??👀** ",
           " **aajao re sav log party ho rhi hai 🎉🏮** ",
           " **chor chor jane de tu yaha aaja 🌸🌝** ",
           " **cutiepie kese ho tum ??🙈** ",
           " **hello broo kaha hai ✌️** ",
           " **oyee dairy milk khaoge 😉😋** ",
           " **kaha gya baandar 🧐** ",
           " **tere bina lagda ni jii mera 🥺** ",
           ]

ENGES = [ " **GooD MorninG 😊❣️** ",
           " **How are you ?? 🤌👀** ",
           " **Hey ! What are you doing 🌝👀 ??** ",
           " **Have a nice day 🦋🕊** ",
           " **Please come to the group and join vc 😊❤️** ",
           " **Hello beby, come here 🌸🥀** ",
           " **Join vc and enjoy Music 🐣🌺** ",
           " **What are you doing 🙄 ??** ",
           " **Miss you beby 🥺💞** ",
           " **Have you had breakfast ?? 🥂🐬** ",
           " **Where are you busy 😒😒 ??** ",
           " **Why are you sad 🙁✨ ??** ",
           " **Love you sweetheart ❤️🙈** ",
           " **What did they say 🤔🤔 ??** ",
           " **How old are you 🤓🤓 ??** ",
           " **Holla Beby 😘❤️** ",
           " **Please come online i waana to talk with you 🥹❤️‍🩹** ",
           " **You forgot me 🙂💔** ",
           " **Where are you going ?? 🐣😿** ",
           " **What happened today ?? 🥴** ",
           " **Beby, please give me a kitkat 😋🍫** ",
           " **Tell me what will you eat 😊✨ ??** ",
           " **Hey, listen cutie 🙈😁** ",
           " **You are looking so hot 😆🌷** ",
           " **Hello friend, where are you? 😁🎊** ",
           " **Good Night Beby 🌙🌚** ",
           " **Come vc and talk 😌🥀** ",
           " **How is your health? 🤌🥺** ",
           " **Have breakfast without me 😒😅** ",
           " **Are you comdey me 😂😂 ??** ",
           " **Did your have your meal ☺️ ?** ",
           " **Do you see a broken star? 😇🥰** ",
           " **I'm always with you 😁❤️** ",
           " **How is life going ?? ✨🌝** ",
           " **Where are you today 🍃🌼 ??** ",
           " **Can we meet ??** ",
           " **Why are you feeling alone?🫶❤️** ",
           " **Let me tell you one thing, I love you ❤️🫰** ",
           " **Where are you ?? 😶** ",
           " **You broke up with your girlfriend 😢💔** ",
           " **No one loves me 😔❤️** ",
           " **Do you have a gf 😒 ??** ",
           " **GooD Night 🌙🌚** ",
           " **Take care 🥀🫶** ",
           " **See you soon ✨🦋** ",
           " **Get up, it's morning 😁🍒** ",
           " **Hii handsome 🌝❤️** ",
           " **Do you love me or not 🐣💖 ??** ",
           " **Let's naccho 🌝🌸** ",
           " **Come baby - @Moiii_World** ",
        ]


@client.on(events.NewMessage(pattern="^/hstag ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("_Only admin can tag all the members_...")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("/hstag hello for tgagging members")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.respond("/hstag hello for tagging members")
        if msg == None:
            return await event.respond(
                "/hstag hello type for tagging members"
            )
    else:
        return await event.respond(
            "/hstag hii type like this for tagging members"

        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtext = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtext += f"[ {usr.first_name} ](tg://user?id={usr.id}) "
 
        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtext} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtext = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@client.on(events.NewMessage(pattern="^/eftag ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("_Only admin can tag all the members_...")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("/eftag hello for tgagging members")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.respond("/eftag hello for tagging members")
        if msg == None:
            return await event.respond(
                "/eftag reply ang message"
            )
    else:
        return await event.respond(
            "/eftag hello for tagging members"

        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrftext = ""
    usrftuxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrftext += f"[ {usr.first_name} ](tg://user?id={usr.id}) "
 
        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrftext} {random.choice(ENGES)}"
                await client.send_message(chat_id, txt)
            await asyncio.sleep(2)
            usrnum = 0
            usrftext = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("_Only admin can tag all the members_...")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("/hstag hello for tgagging members")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "/etag reply any msg for tagging"
            )
    else:
        return await event.respond(
            "/etag reply any msg for tagging"

        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrEMtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrEMtxt += f"[{random.choice(EMOJI)}](tg://user?id={usr.id}) "
 
        if usrnum == 4:
            if mode == "text_on_reply":
               await msg.reply(usrEMtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrEMtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@client.on(events.NewMessage(pattern="^/ftag ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("_Only admin can tag all the members_...")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("/ftag hello for tgagging members")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "/ftag reply any msg for tagging"
            )
    else:
        return await event.respond(
            "/ftag reply any msg for tagging"

        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrFGtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrFGtxt += f"[{random.choice(FLAGS)}](tg://user?id={usr.id}) "
 
        if usrnum == 4:
            if mode == "text_on_reply":
               await msg.reply(usrFGtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrFGtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/tagall ?(.*)"))
@client.on(events.NewMessage(pattern="^@all ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )
    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__Only admins can mention all!__")
    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("__Give me one argument!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__I can't mention members for older messages! (messages which are sent before I'm added to group)__"
            )
    else:
        return await event.respond(
            "__Reply to a message or give me some text to mention others!__"
        )
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{msg}\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(3)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("__There is no proccess on going...__")
    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__Only admins can execute this command!__")

    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("__Stopped Mention.__")


__mod_name__ = "Tᴀɢ Aʟʟ"
__help__ = """
──「 Only for Admins 」──

❍ /tagall or @all (reply to message or add another message) To mention all members in your group, without exception.
❍ /hstag (add another message) To mention all members in your group, with special hinglish tagger.
❍ /etag (reply to message) To mention all members in your group, with special emoji tagger.
❍ /eftag (add another message) To mention all members in your group, with special english tagger.
❍ /ftag (reply to message) To mention all members in your group, with special flag tagger.

"""
