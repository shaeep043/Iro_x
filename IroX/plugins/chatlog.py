import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import LOG_GROUP_ID
from IroX import app  

photo = [
    "https://telegra.ph/file/52f7f43d1657f63bfddd7.jpg",
    "https://telegra.ph/file/17b68f97a97d57c426cd0.jpg",
    "https://telegra.ph/file/364d0f7a474ae0427eeef.jpg",
    "https://telegra.ph/file/21fc071d44e1a449e8443.jpg",
    "https://telegra.ph/file/4614e9432c2fb7095a871.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**♡ ɴᴇᴡ ɢʀᴏᴜᴘ ✩**\n\n"
                f"**ᴄʜᴀᴛ ɴᴀᴍᴇ:** {message.chat.title}\n"
                f"**ᴄʜᴀᴛ ɪᴅ:** {message.chat.id}\n"
                f"**ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ:** @{message.chat.username}\n"
                f"**ᴄʜᴀᴛ ʟɪɴᴋ:** [ᴄʟɪᴄᴋ]({link})\n"
                f"**ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs:** {count}\n"
                f"**ᴀᴅᴅᴇᴅ ʙʏ:** {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f" ɢʀᴏᴜᴘ ", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜꜱᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        chat_id = message.chat.id
        left = f"**✩** <b><u>#ʟᴇꜰᴛ_ɢʀᴏᴜᴘ</u></b> **★**\n\n**ᴄʜᴀᴛ ᴛɪᴛʟᴇ :** {title}\n\n**ᴄʜᴀᴛ ɪᴅ :** {chat_id}\n\n**ʀᴇᴍᴏᴠᴇ ʙʏ :** {remove_by}\n\n**ʙᴏᴛ : @{app.username}**"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
