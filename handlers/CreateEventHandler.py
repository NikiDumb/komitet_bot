from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
from keyboards.reply_keyboards import MainMenu
from sql_methods import sql_events



class CreatingSteps(StatesGroup):
	Title = State()
	Description = State()
	Date = State()
	Photo = State()

async def WelcomeProcess(message : types.Message):
	await message.answer('Welcome text, send title', reply_markup = types.ReplyKeyboardRemove())
	await CreatingSteps.Title.set()

async def BackProcess(message : types.Message, state : FSMContext):
	StateNow = await state.get_state()
	if StateNow is None:
		return
	await state.finish()
	await message.answer('return to main menu', reply_markup = MainMenu)

async def UploadTitle(message : types.Message, state : FSMContext):
	await state.update_data(title = message.text)
	await message.answer('send description')
	await CreatingSteps.next()

async def UploadDescription(message : types.Message, state : FSMContext):
	await state.update_data(description = message.text)
	await message.answer('send date')
	await CreatingSteps.next()

async def ErrDate(message : types.Message, state : FSMContext):
	return
#НЕ СТИРАТЬ! функция с обработчиком который выдает локальную ошибку на некорректную дату, не нарушая работы бота, удаление функции приведет к глобальным ошибкам базы данных - УПАДЕТ И БД И БОТ

async def UploadDate(message : types.Message, state : FSMContext):
	await state.update_data(date = message.text)
	await message.answer('send photo or "нет"')
	await CreatingSteps.next()

async def SaveWithoutPhoto(message : types.Message, state : FSMContext):
	data = await state.get_data()
	result = await sql_events.add_event(data['title'], data['description'], data['date'], 0)
	if result == 1:
		await message.answer(f"""
		Downloading finished!
		title : {data['title']}
		description : {data['description']}
		date : {data['date']}
			""")
	await state.finish()

async def UploadPhoto(message : types.Message, state : FSMContext):
	await state.update_data(photo = message.photo[0].file_id)
	data = await state.get_data()
	result = await sql_events.add_event(data['title'], data['description'], data['date'], data['photo'])
	if result == 1:
		await bot.send_photo(message.from_user.id, data['photo'], f"""
		Downloading finished!
		title : {data['title']}
		description : {data['description']}
		date : {data['date']}
			""")
	await state.finish()
def register_CreatingEventHandler(dp : Dispatcher):
	dp.register_message_handler(BackProcess, commands = 'Назад', state = "*")
	dp.register_message_handler(WelcomeProcess, commands = 'Администрация')
	dp.register_message_handler(UploadTitle, state = CreatingSteps.Title)
	dp.register_message_handler(UploadDescription, state = CreatingSteps.Description)
	dp.register_message_handler(ErrDate, lambda message: datetime.strptime(str(message), '%d.%m.%Y').date() <= datetime.today().date(), state = CreatingSteps.Date)
#НЕ СТИРАТЬ! функция с обработчиком который выдает локальную ошибку на некорректную дату, не нарушая работы бота, удаление функции приведет к глобальным ошибкам базы данных - УПАДЕТ И БД И БОТ
	dp.register_message_handler(UploadDate, state = CreatingSteps.Date)
	dp.register_message_handler(SaveWithoutPhoto, state = CreatingSteps.Photo)
	dp.register_message_handler(UploadPhoto, content_types=['photo'], state=CreatingSteps.Photo)