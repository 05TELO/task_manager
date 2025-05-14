import asyncio
import logging
import sys

from bot.bot import create_bot, create_dispatcher
from bot.config import TG_BOT_SECRET

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)

if __name__ == "__main__":
    if not TG_BOT_SECRET:
        msg = "TELEGRAM_BOT_TOKEN не установлен"
        raise ValueError(msg)

    dp = create_dispatcher()
    bot = create_bot(TG_BOT_SECRET)

    asyncio.run(dp.start_polling(bot))
