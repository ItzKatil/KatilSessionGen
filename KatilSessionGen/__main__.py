import asyncio
import importlib

from pyrogram import idle

from KatilSessionGen import LOGGER, Katil
from KatilSessionGen.modules import ALL_MODULES


async def Katil_boot():
    try:
        await Katil.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("KatilSessionGen.modules." + all_module)

    LOGGER.info(f"@{Katil.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Katil_boot())
    LOGGER.info("Stopping String Gen Bot...")
