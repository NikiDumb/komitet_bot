from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()
bot = Bot(token='5462351629:AAGLmPHbWsc8LOv2A9V7jhHkCtB0TjJgBbk', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)