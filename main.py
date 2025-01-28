from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import Config

# Инициализация бота и диспетчера
bot = Bot(token=Config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if __name__ == "__main__":
    from bot.handlers import register_handlers
    register_handlers(dp)  # Регистрация обработчиков
    executor.start_polling(dp, skip_updates=True)