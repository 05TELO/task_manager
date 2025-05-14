from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


COMMANDS_LIST = {
    "/start": "Показать приветствие и список команд",
    "/mytasks": "Показать все мои активные задачи",
    "/done {ID задачи}": "Отметить задачу как выполненную",
}


def generate_help_text() -> str:
    help_text = "<b>🛠 Доступные команды:</b>\n\n"
    for cmd, desc in COMMANDS_LIST.items():
        help_text += f"<code>{cmd}</code> — {desc}\n"
    return help_text


@router.message(Command("start"))
async def command_start(message: Message):
    welcome_text = (
        f"<b>🚀 Добро пожаловать в Task Manager Bot!</b>\n\n{generate_help_text()}\n\n"
    )
    await message.answer(welcome_text, parse_mode=ParseMode.HTML)
