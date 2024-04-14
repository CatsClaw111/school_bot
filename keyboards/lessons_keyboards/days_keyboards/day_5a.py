from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_5, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_5a_mon = KeyboardButton(text='Понедельник_5А')
but_5a_tue = KeyboardButton(text='Понедельник_5А')
but_5a_wed = KeyboardButton(text='Понедельник_5А')
but_5a_thu = KeyboardButton(text='Понедельник_5А')
but_5a_fri = KeyboardButton(text='Понедельник_5А')

days_5a_key = ReplyKeyboardMarkup(
    keyboard=[[but_5a_mon, but_5a_tue, but_5a_wed],
              [but_5a_thu, but_5a_fri],
              [but_ret_class_5, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)