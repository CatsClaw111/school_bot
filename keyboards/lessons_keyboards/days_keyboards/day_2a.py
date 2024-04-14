from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_2, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_2a_mon = KeyboardButton(text='Понедельник_2А')
but_2a_tue = KeyboardButton(text='Понедельник_2А')
but_2a_wed = KeyboardButton(text='Понедельник_2А')
but_2a_thu = KeyboardButton(text='Понедельник_2А')
but_2a_fri = KeyboardButton(text='Понедельник_2А')

days_2a_key = ReplyKeyboardMarkup(
    keyboard=[[but_2a_mon, but_2a_tue, but_2a_wed],
              [but_2a_thu, but_2a_fri],
              [but_ret_class_2, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)
