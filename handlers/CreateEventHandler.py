from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime



class CreatingSteps(StatesGroup):
	Title = State()
	Description = State()
	Date = State()
	Photo = State()

async def BackProcess(message : types.Message):
	await message.answer('return to main menu')

async def WelcomeProcess(message : types.Message):
	await message.answer('Welcome text, send title')
	await CreatingSteps.Title.set()

async def UploadTitle(message : types.Message, state : FSMContext):
	async with state.proxy() as data:
		data['title'] = message.text
	await message.answer('send description')
	await CreatingSteps.next()

async def UploadDescription(message : types.Message, state : FSMContext):
	async with state.proxy() as data:
		data['description'] = message.text
	await message.answer('send date')
	await CreatingSteps.next()

async def ErrDate(message : types.Message, state : FSMContext):
	await message.answer('bad date')

async def UploadDate(message : types.Message, state : FSMContext):







def register_CreatingEventHandler(dp : Dispatcher):

