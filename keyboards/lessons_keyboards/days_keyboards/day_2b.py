from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_2, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_2b_mon = KeyboardButton(text='Понедельник_2Б')
but_2b_tue = KeyboardButton(text='Понедельник_2Б')
but_2b_wed = KeyboardButton(text='Понедельник_2Б')
but_2b_thu = KeyboardButton(text='Понедельник_2Б')
but_2b_fri = KeyboardButton(text='Понедельник_2Б')

days_2b_key = ReplyKeyboardMarkup(
    keyboard=[[but_2b_mon, but_2b_tue, but_2b_wed],
              [but_2b_thu, but_2b_fri],
              [but_ret_class_2, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)
