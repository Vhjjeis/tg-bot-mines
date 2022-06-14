from aiogram import executor
from handlers import dp
from loader import bot
import logger


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
