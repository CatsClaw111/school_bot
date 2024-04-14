from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_1, but_ret_par, but_ret_menu

but_1a_mon = KeyboardButton(text='Понедельник_1А')
but_1a_tue = KeyboardButton(text='Понедельник_1А')
but_1a_wed = KeyboardButton(text='Понедельник_1А')
but_1a_thu = KeyboardButton(text='Понедельник_1А')
but_1a_fri = KeyboardButton(text='Понедельник_1А')

days_1_key = ReplyKeyboardMarkup(
    keyboard=[[but_1a_mon, but_1a_tue, but_1a_wed],
              [but_1a_thu, but_1a_fri]
              [but_ret_class_1, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)
