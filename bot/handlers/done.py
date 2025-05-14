import httpx
from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

from bot.services.task_api import get_httpx_client

router = Router()


@router.message(Command("done"))
async def command_done(message: Message, command: Command):
    if not command.args:
        await message.answer(
            "<b>❌ Укажите ID задачи:</b> <code>/done {ID задачи}</code>",
            parse_mode=ParseMode.HTML,
        )
        return

    try:
        task_id = int(command.args)
    except ValueError:
        await message.answer("<b>❌ ID задачи должен быть числом</b>")
        return

    try:
        async with get_httpx_client() as client:
            update_response = await client.patch(
                f"/tasks/{task_id}/", json={"status": "done"}
            )
            update_response.raise_for_status()

    except httpx.HTTPStatusError:
        await message.answer(
            "<b>⚠️ Ошибка при получении задач. Попробуйте позже.</b>",
            parse_mode=ParseMode.HTML,
        )
    else:
        await message.answer(f"<b>✅ Задача {task_id} отмечена как выполненная!</b>")
