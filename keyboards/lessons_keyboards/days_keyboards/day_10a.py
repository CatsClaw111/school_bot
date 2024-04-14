from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_10, but_ret_par, but_ret_menu

but_10a_mon = KeyboardButton(text='Понедельник_10А')
but_10a_tue = KeyboardButton(text='Понедельник_10А')
but_10a_wed = KeyboardButton(text='Понедельник_10А')
but_10a_thu = KeyboardButton(text='Понедельник_10А')
but_10a_fri = KeyboardButton(text='Понедельник_10А')

days_10a_key = ReplyKeyboardMarkup(
    keyboard=[[but_10a_mon, but_10a_tue, but_10a_wed],
              [but_10a_thu, but_10a_fri]
              [but_ret_class_10, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)