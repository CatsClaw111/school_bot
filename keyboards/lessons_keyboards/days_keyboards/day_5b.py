from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_5, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_5b_mon = KeyboardButton(text='Понедельник_5Б')
but_5b_tue = KeyboardButton(text='Понедельник_5Б')
but_5b_wed = KeyboardButton(text='Понедельник_5Б')
but_5b_thu = KeyboardButton(text='Понедельник_5Б')
but_5b_fri = KeyboardButton(text='Понедельник_5Б')

days_5b_key = ReplyKeyboardMarkup(
    keyboard=[[but_5b_mon, but_5b_tue, but_5b_wed],
              [but_5b_thu, but_5b_fri]
              [but_ret_class_5, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)