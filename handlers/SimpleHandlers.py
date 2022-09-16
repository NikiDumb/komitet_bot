from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from keyboards.reply_keyboards import MainMenu, MenuNotsNil
from keyboards.inline_keyboards import TiosMenu, SubMenu

async def WelcomeProcess(message: types.Message):
	#Получить id пользователя и проверить есть ли он в списках администрации
	await message.answer(f"{message.from_user.full_name} something welcome text", reply_markup = MainMenu)

async def NotsNilProcess(message: types.Message):
	await message.answer("smthng nots nil info", reply_markup = MenuNotsNil)

async def ContactsProcess(message: types.Message):
	await message.answer("smthng contacts", reply_markup = MainMenu)

async def AboutProcess(message: types.Message):
	await message.answer("smthng about", reply_markup = MainMenu)

async def SubsProcess(message: types.Message):
	await message.answer("destroy keyboards", reply_markup = types.ReplyKeyboardRemove())
	await message.answer("smthng subs main", reply_markup = SubMenu)

async def TiosProcess(message: types.Message):
	await message.answer("destroy keyboards", reply_markup = types.ReplyKeyboardRemove())
	await message.answer("smthng tios words", reply_markup = TiosMenu)





async def BackCallback(callback : types.CallbackQuery):
	await callback.message.answer('return to main menu', reply_markup = MainMenu)

async def TiosCallback(callback : types.CallbackQuery):
	result = callback.data.split('_')[2]
	if result == "info":
		await callback.message.answer('tios info')
	elif result == "achievments":
		await callback.message.answer('tios achievments')
	elif result == "contacts":
		await callback.message.answer('tios contacts')


def register_SimpleHandlers(dp : Dispatcher):
	dp.register_message_handler(WelcomeProcess, commands=['Start'])
	dp.register_message_handler(NotsNilProcess, commands=['НОЦЫ_НИЛЫ'])
	dp.register_message_handler(ContactsProcess, commands=['Контакты'])
	dp.register_message_handler(AboutProcess, commands=['О_комитете'])
	dp.register_message_handler(SubsProcess, commands=['Подписки'])
	dp.register_message_handler(TiosProcess, commands=['ТИОС'])


	dp.register_callback_query_handler(TiosCallback, Text(startswith="tios_button_"))
	dp.register_callback_query_handler(BackCallback, Text(startswith="go_back")) #Заменить текст на лямбда функцию
