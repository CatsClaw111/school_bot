from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_11, but_ret_par, but_ret_menu

but_11a_mon = KeyboardButton(text='Понедельник_11А')
but_11a_tue = KeyboardButton(text='Понедельник_11А')
but_11a_wed = KeyboardButton(text='Понедельник_11А')
but_11a_thu = KeyboardButton(text='Понедельник_11А')
but_11a_fri = KeyboardButton(text='Понедельник_11А')

days_11a_key = ReplyKeyboardMarkup(
    keyboard=[[but_11a_mon, but_11a_tue, but_11a_wed],
              [but_11a_thu, but_11a_fri]
              [but_ret_class_11, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)