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
from keyboards.reply_keyboards import EventTypeMenu, MainMenu
import re 



class CreatingSteps(StatesGroup):
	Title = State()
	Type = State()
	Description = State()
	Date = State()
	WebSource = State()
	Photo = State()


async def WelcomeProcess(message : types.Message):
	await message.answer('Welcome text, send title', reply_markup = types.ReplyKeyboardRemove())
	await CreatingSteps.Title.set()

async def UploadTitle(message : types.Message, state : FSMContext):
	await state.update_data(title = message.text)
	await message.answer('Choose type', reply_markup = EventTypeMenu)
	await CreatingSteps.next()

async def ChooseType(message : types.Message, state : FSMContext):
	if message.text == 'Внутреннее' or message.text == 'Внешнее':
		await state.update_data(type = message.text)
		await message.answer('send description', reply_markup = types.ReplyKeyboardRemove())
		await CreatingSteps.next()
	else:
		await message.reply(f'fuck you, {message.from_user.full_name}, try again', reply_markup = EventTypeMenu)
		return

async def UploadDescription(message : types.Message, state : FSMContext):
	await state.update_data(description = message.text)
	await message.answer('send date')
	await CreatingSteps.next()

async def UploadDate(message : types.Message, state : FSMContext):
	await state.update_data(date = message.text)
	await message.answer('send web resourse or "нет"')
	await CreatingSteps.next()

async def ErrDate(message : types.Message, state : FSMContext):
	await message.reply(f'fuck you, {message.from_user.full_name}, try again')
	return

async def UploadWebSource(message : types.Message, state : FSMContext):
	await state.update_data(source = message.text)
	await message.answer('send photo or "нет"')
	await CreatingSteps.next()

async def ErrWebSource(message : types.Message, state : FSMContext):
	if message.text == 'нет':
		await state.update_data(source = 0)
		await message.answer('send photo or "нет"')
		await CreatingSteps.next()
	else:
		await message.reply(f'fuck you, {message.from_user.full_name}, try again')
		return

async def SaveWithoutPhoto(message : types.Message, state : FSMContext):
	data = await state.get_data()
	result = await sql_events.add_event(data['title'], data['type'], data['description'], data['date'], 0, 0, data['source'])
	if result == 1:
		if data['source'] == 0: data['source'] = 'without source'
		await message.answer(f"""
	Downloading finished!
	+title : {data['title']}
	+type : {data['type']}
	+description : {data['description']}
	+date : {data['date']}
	+web resource : {data['source']}
	-without photo
			""", reply_markup = MainMenu)
	await state.finish()

async def UploadPhoto(message : types.Message, state : FSMContext):
	await state.update_data(photo = message.photo[0].file_id)
	data = await state.get_data()
	result = await sql_events.add_event(data['title'], data['type'], data['description'], data['date'], data['photo'], 0, data['source'])
	if result == 1:
		if data['source'] == 0: data['source'] = 'without source'
		await bot.send_photo(message.from_user.id, data['photo'], f"""
		Downloading finished!
	+title : {data['title']}
	+type : {data['type']}
	+description : {data['description']}
	+date : {data['date']}
	+web resource : {data['source']}
			""", reply_markup = MainMenu)
	await state.finish()
def register_CreatingEventHandler(dp : Dispatcher):
	dp.register_message_handler(WelcomeProcess, commands = 'Администрация')
	dp.register_message_handler(UploadTitle, state = CreatingSteps.Title)
	dp.register_message_handler(ChooseType, state = CreatingSteps.Type)
	dp.register_message_handler(UploadDescription, state = CreatingSteps.Description)
	dp.register_message_handler(UploadDate, lambda message: re.findall(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})",message.text), state = CreatingSteps.Date)
	dp.register_message_handler(ErrDate, state = CreatingSteps.Date)
	dp.register_message_handler(UploadWebSource, lambda message: re.search(r'(https?://[\S]+)', message.text), state = CreatingSteps.WebSource)
	dp.register_message_handler(ErrWebSource, state = CreatingSteps.WebSource)
	dp.register_message_handler(SaveWithoutPhoto, state = CreatingSteps.Photo)
	dp.register_message_handler(UploadPhoto, content_types=['photo'], state=CreatingSteps.Photo)