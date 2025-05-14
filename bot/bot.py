from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers.done import router as done_router
from bot.handlers.mytasks import router as mytasks_router
from bot.handlers.start import router as start_router


def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(mytasks_router)
    dp.include_router(done_router)
    return dp


def create_bot(token: str) -> Bot:
    return Bot(
        token=token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
