from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_7, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_7a_mon = KeyboardButton(text='Понедельник_7А')
but_7a_tue = KeyboardButton(text='Понедельник_7А')
but_7a_wed = KeyboardButton(text='Понедельник_7А')
but_7a_thu = KeyboardButton(text='Понедельник_7А')
but_7a_fri = KeyboardButton(text='Понедельник_7А')

days_7a_key = ReplyKeyboardMarkup(
    keyboard=[[but_7a_mon, but_7a_tue, but_7a_wed],
              [but_7a_thu, but_7a_fri],
              [but_ret_class_7, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)