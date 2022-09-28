from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class UserStates(StatesGroup):
	admin = State() #администратор
	komitet = State() #член комитета
	user = State() #верифицированный пользователь
