from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from sql_methods import sql_lists
from keyboards.inline_keyboards import SubMenu


async def SubCallback(callback : types.CallbackQuery):
	result = callback.data.split('_')[2]
	if result == "all":
		await callback.message.answer('sub all', reply_markup = types.ReplyKeyboardRemove())
	elif result == "inside":
		InsideSubDataResult = await sql_lists.add_sub_inside(callback.from_user.id)
		if InsideSubDataResult == 1:
			await callback.answer('sub inside', show_alert=True )
		elif InsideSubDataResult == 606:
			await callback.answer('already sub', show_alert=True )
	elif result == "outside":
		await callback.message.answer('sub outside', reply_markup = types.ReplyKeyboardRemove())
	elif result == "unsub":
		UnsubDataResult = await sql_lists.delete_inside_sub(callback.from_user.id)
		if UnsubDataResult == 1:
			await callback.answer('unsub all', show_alert=True )
		elif UnsubDataResult == 404:
			await callback.answer('already unsub all', show_alert=True )

def register_SubHandlers(dp : Dispatcher):
	dp.register_callback_query_handler(SubCallback, Text(startswith="sub_button_"))