from aiogram.utils import executor
from create_bot import dp, bot
import os
async def on_startup(_):
	os.system('cls')
	print('Мы вышли в онлайн. Закройте это окно чтобы прекратить работу')
from handlers import SimpleHandlers, SubHandlers, CreateEventHandler
try:
	SimpleHandlers.register_SimpleHandlers(dp)
	SubHandlers.register_SubHandlers(dp)
	CreateEventHandler.register_CreatingEventHandler(dp)
	executor.start_polling(dp, skip_updates = True, on_startup = on_startup)
except Exception as e:
	print(e)