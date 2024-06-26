import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import main_handlers, break_schedule_handlers, teacher_hadlers
from handlers.lessons_schedule_handlers import parallel_schedule_handlers, class_schedule_handlers, days_handlers

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')
    dp = Dispatcher()

    dp.include_routers(main_handlers.router, parallel_schedule_handlers.router, class_schedule_handlers.router,
                       break_schedule_handlers.router, days_handlers.router, teacher_hadlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
