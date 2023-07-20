import asyncio 
import config
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import MUSIC_BOT_NAME, LOG_GROUP_ID, PLAYLIST_IMG_URL, PRIVATE_BOT_MODE, adminlist
from strings import get_string
from IroX import YouTube, app, userbot
from IroX.misc import SUDOERS
from IroX.utils.database import (get_cmode, get_lang,
                                       get_playmode, get_playtype,
                                       is_active_chat,
                                       is_commanddelete_on,
                                       is_served_private_chat)
from IroX.utils.exceptions import AssistantErr
from IroX.utils.database.assistantdatabase import get_assistant
from IroX.utils.database.memorydatabase import is_maintenance
from IroX.utils.inline.playlist import botplaylist_markup


def PlayWrapper(command):
    async def wrapper(client, message):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    "» ʙᴏᴛ ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ғᴏʀ sᴏᴍᴇ ᴛɪᴍᴇ, ᴩʟᴇᴀsᴇ ᴠɪsɪᴛ [sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ](https://t.me/THE_THIRD_EYE_NETWORK) ᴛᴏ ᴋɴᴏᴡ ᴛʜᴇ ʀᴇᴀsᴏɴ..."
                )
        if PRIVATE_BOT_MODE == str(True):
            if not await is_served_private_chat(message.chat.id):
                await message.reply_text(
                    "**ᴩʀɪᴠᴀᴛᴇ ᴍᴜsɪᴄ ʙᴏᴛ**\n\nᴏɴʟʏ ғᴏʀ ᴛʜᴇ ᴄʜᴀᴛs ᴀᴜᴛʜᴏʀɪsᴇᴅ ʙʏ ᴛʜᴇ ᴏᴡɴᴇʀ. ʀᴇǫᴜᴇsᴛ ɪɴ ᴍʏ ᴏᴡɴᴇʀ's ᴩᴍ ᴛᴏ ᴀᴜᴛʜᴏʀɪsᴇ ʏᴏᴜʀ ᴄʜᴀᴛ ғᴏʀ ᴜsɪɴɢ ᴍᴇ."
                )
                return await app.leave_chat(message.chat.id)
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        audio_telegram = (
            (
                message.reply_to_message.audio
                or message.reply_to_message.voice
            )
            if message.reply_to_message
            else None
        )
        video_telegram = (
            (
                message.reply_to_message.video
                or message.reply_to_message.document
            )
            if message.reply_to_message
            else None
        )
        url = await YouTube.url(message)
        if (
            audio_telegram is None
            and video_telegram is None
            and url is None
        ):
            if len(message.command) < 2:
                if "stream" in message.command:
                    return await message.reply_text(_["str_1"])
                buttons = botplaylist_markup(_)
                return await message.reply_photo(
                    photo=PLAYLIST_IMG_URL,
                    caption=_["playlist_1"],
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʜᴏᴡ ᴛᴏ ғɪx ᴛʜɪs ?",
                            callback_data="IroymousAdmin",
                        ),
                    ]
                ]
            )
            return await message.reply_text(
                _["general_4"], reply_markup=upl
            )
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_12"])
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
        else:
            chat_id = message.chat.id
            channel = None
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_18"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])
        if message.command[0][0] == "v":
            video = True
        else:
            if "-v" in message.text:
                video = True
            else:
                video = True if message.command[0][1] == "v" else None
        if message.command[0][-1] == "e":
            if not await is_active_chat(chat_id):
                return await message.reply_text(_["play_18"])
            fplay = True
        else:
            fplay = None
        if not await is_active_chat(chat_id):
            userbot = await get_assistant(chat_id)
            try:
                try:
                    get = await app.get_chat_member(chat_id, userbot.id)
                except ChatAdminRequired:
                    return await message.reply_text(
                        "» ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ **ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ** ғᴏʀ ɪɴᴠɪᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ."
                    )
                if get.status == "banned" or get.status == "kicked":
                    upl = InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text=f"ᴜɴʙᴀɴ {userbot.name}",
                                    callback_data=f"unban_assistant {chat_id}|{userbot.id}",
                                ),
                            ]
                        ]
                    )
                    return await message.reply_text(
                        f"{MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ɪs ʙᴀɴɴᴇᴅ ɪɴ {message.chat.title}.\n\n• **ɪᴅ :** `{userbot.id}`\n• **ᴜsᴇʀɴᴀᴍᴇ :** @{userbot.username}\n\n» ᴘʟᴇᴀsᴇ ᴜɴʙᴀɴ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀɴᴅ ᴛʀʏ ᴘʟᴀʏɪɴɢ ᴀɢᴀɪɴ.",
                        reply_markup=upl,
                    )
            except UserNotParticipant:
                chat = await app.get_chat(chat_id)
                if chat.username:
                    try:
                        await userbot.join_chat(chat.username)
                    except UserAlreadyParticipant:
                        pass
                    except Exception as e:
                        raise AssistantErr(_["call_3"].format(e))
                else:
                    try:
                        try:
                            try:
                                invitelink = chat.invite_link
                                if invitelink is None:
                                    invitelink = (
                                        await app.export_chat_invite_link(
                                            chat_id
                                        )
                                    )
                            except:
                                invitelink = (
                                    await app.export_chat_invite_link(
                                        chat_id
                                    )
                                )
                        except ChatAdminRequired:
                            raise AssistantErr(_["call_4"])
                        except Exception as e:
                            raise AssistantErr(e)
                        m = await app.send_message(
                            chat_id, _["call_5"].format(userbot.name, chat.title)
                        )
                        if invitelink.startswith("https://t.me/+"):
                            invitelink = invitelink.replace(
                                "https://t.me/+", "https://t.me/joinchat/"
                            )
                        await asyncio.sleep(1)
                        await userbot.join_chat(invitelink)
                        await m.edit_text(_["call_6"].format(config.MUSIC_BOT_NAME))
                    except UserAlreadyParticipant:
                        pass
                    except Exception as e:
                        raise AssistantErr(_["call_3"].format(e))
        return await command(
            client,
            message,
            _,
            chat_id,
            video,
            channel,
            playmode,
            url,
            fplay,
        )

    return wrapper
