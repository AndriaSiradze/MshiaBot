import logging

from aiogram import Dispatcher
from aiogram import executor
from aiogram.utils.executor import start_webhook

from filters.client_filters import register_client_filters
from handlers.client import register_client_handlers
from tg_bot.create_bot import dp, bot, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT

logger = logging.getLogger(__name__)


def register_all_handlers(dp: Dispatcher):
    register_client_handlers(dp)


def register_all_filters(dp: Dispatcher):
    register_client_filters(dp)


async def on_startup(_):
    logging.basicConfig(
        level=logging.INFO,
        format=u"%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s"
    )
    # Set webhook
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=False)

    # registration handlers,filters,middlewares
    register_all_filters(dp)
    register_all_handlers(dp)

    print("Bot is Online")


async def on_shutdown(_):
    await bot.delete_webhook()
    print("Bot is Offline")


start_webhook(
    dispatcher=dp,
    webhook_path=WEBHOOK_PATH,
    skip_updates=True,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    host=WEBAPP_HOST,
    port=WEBAPP_PORT,
)
# executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
