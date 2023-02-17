from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from config import API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Позваляет хранить данные в оперативное памяти
from src.handlers import register_grants

storage = MemoryStorage()
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)


async def on_starttup(_):
    print("Бот запущен!")


def start_event_loop():
    start_system = register_grants.RegisterGrant(dp)
    start_system.register_handlers_system()
    executor.start_polling(dp, skip_updates=True, on_startup=on_starttup)


if __name__ == "__main__":
    start_event_loop()
