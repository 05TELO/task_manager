import httpx
from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

from bot.services.task_api import get_httpx_client
from bot.utils.date_format import format_datetime

router = Router()


@router.message(Command("mytasks"))
async def command_mytasks(message: Message):
    try:
        async with get_httpx_client() as client:
            response = await client.get(
                "/tasks/", params={"search": message.from_user.id}
            )
            response.raise_for_status()
    except httpx.HTTPStatusError:
        await message.answer(
            "<b>⚠️ Ошибка при получении задач. Попробуйте позже.</b>",
            parse_mode=ParseMode.HTML,
        )
    tasks = response.json()["results"]
    if not tasks:
        await message.answer("У вас нет активных задач!")
        return

    tasks_text = "<b>📋 Ваши активные задачи:</b>\n\n"
    for task in tasks:
        status_emoji = "✅" if task["status"] == "done" else "🟡"
        status_text = "Выполнена" if task["status"] == "done" else "В процессе"
        deadline = format_datetime(task["deadline"])

        tasks_text += (
            f"<b>ID:</b> <code>{task['id']}</code>\n"
            f"<b>Название:</b> {task['title']}\n"
            f"<b>Описание:</b> {task['description'] or 'отсутствует'}\n"
            f"<b>Срок:</b> <code>{deadline}</code>\n"
            f"<b>Статус:</b> {status_emoji} {status_text}\n\n"
        )

    await message.answer(tasks_text.strip(), parse_mode=ParseMode.HTML)
