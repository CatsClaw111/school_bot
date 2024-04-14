from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_6, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_6b_mon = KeyboardButton(text='Понедельник_6Б')
but_6b_tue = KeyboardButton(text='Понедельник_6Б')
but_6b_wed = KeyboardButton(text='Понедельник_6Б')
but_6b_thu = KeyboardButton(text='Понедельник_6Б')
but_6b_fri = KeyboardButton(text='Понедельник_6Б')

days_6b_key = ReplyKeyboardMarkup(
    keyboard=[[but_6b_mon, but_6b_tue, but_6b_wed],
              [but_6b_thu, but_6b_fri],
              [but_ret_class_6, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)