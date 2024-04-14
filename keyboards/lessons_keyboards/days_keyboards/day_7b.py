from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_7, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_7b_mon = KeyboardButton(text='Понедельник_7Б')
but_7b_tue = KeyboardButton(text='Понедельник_7Б')
but_7b_wed = KeyboardButton(text='Понедельник_7Б')
but_7b_thu = KeyboardButton(text='Понедельник_7Б')
but_7b_fri = KeyboardButton(text='Понедельник_7Б')

days_7b_key = ReplyKeyboardMarkup(
    keyboard=[[but_7b_mon, but_7b_tue, but_7b_wed],
              [but_7b_thu, but_7b_fri],
              [but_ret_class_7, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)