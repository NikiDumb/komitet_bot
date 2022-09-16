from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


MainButton_1 = KeyboardButton('/НОЦЫ_НИЛЫ')
MainButton_2 = KeyboardButton('/Контакты')
MainButton_3 = KeyboardButton('/О_комитете')
MainButton_4 = KeyboardButton('/Подписки')
MainButton_5 = KeyboardButton('/Администрация')
MainMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(MainButton_1, MainButton_2, MainButton_3).row(MainButton_4, MainButton_5)

NotsNilButton_1 = KeyboardButton('/ТИОС')
NotsNilButton_2 = KeyboardButton('БИС')
NotsNilButton_3 = KeyboardButton('Прочее')
NotsNilButton_4 = KeyboardButton('Назад')
MenuNotsNil = ReplyKeyboardMarkup(resize_keyboard=True).row(NotsNilButton_1, NotsNilButton_2, NotsNilButton_3).row(NotsNilButton_4)


