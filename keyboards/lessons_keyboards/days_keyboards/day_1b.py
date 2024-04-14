from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_1, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_1b_mon = KeyboardButton(text='Понедельник_1Б')
but_1b_tue = KeyboardButton(text='Понедельник_1Б')
but_1b_wed = KeyboardButton(text='Понедельник_1Б')
but_1b_thu = KeyboardButton(text='Понедельник_1Б')
but_1b_fri = KeyboardButton(text='Понедельник_1Б')

days_1b_key = ReplyKeyboardMarkup(
    keyboard=[[but_1b_mon, but_1b_tue, but_1b_wed],
              [but_1b_thu, but_1b_fri],
              [but_ret_class_1, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)
