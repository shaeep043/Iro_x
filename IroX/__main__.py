import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from IroX import LOGGER, app, userbot
from IroX.core.call import Iro
from IroX.plugins import ALL_MODULES
from IroX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("IroX").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("IroX").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("IroX.plugins." + all_module)
    LOGGER("IroX.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Iro.start()
    try:
        await Iro.stream_decall("https://te.legra.ph/file/3792745d1db27cbe02cdd.mp4")
    except:
        pass
    try:
        await Iro.stream_call(
            "https://te.legra.ph/file/3792745d1db27cbe02cdd.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("IroX").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Iro.decorators()
    LOGGER("IroX").info("\x49\x52\x4f\x20\x58\x20\x4d\x75\x73\x69\x63\x20\x62\x6f\x74\x20\x73\x74\x61\x72\x74\x20\x73\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\x2e\x2e\xf0\x9f\x98\x88\x20\x4e\x6f\x77\x20\x63\x6f\x6d\x65\x20\x74\x6f\x20\x6a\x6f\x69\x6e\x20\x69\x6e\x20\x6f\x75\x72\x20\x73\x75\x70\x70\x6f\x72\x74\x20\x67\x72\x6f\x75\x70\x20\x40\x49\x72\x6f\x5f\x78\x5f\x73\x75\x70\x70\x6f\x72\x74\x20")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("IroX").info("Stopping Music Bot...")
