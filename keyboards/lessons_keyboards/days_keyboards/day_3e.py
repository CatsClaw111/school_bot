from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_3, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_3e_mon = KeyboardButton(text='Понедельник_3Э')
but_3e_tue = KeyboardButton(text='Понедельник_3Э')
but_3e_wed = KeyboardButton(text='Понедельник_3Э')
but_3e_thu = KeyboardButton(text='Понедельник_3Э')
but_3e_fri = KeyboardButton(text='Понедельник_3Э')

days_3e_key = ReplyKeyboardMarkup(
    keyboard=[[but_3e_mon, but_3e_tue, but_3e_wed],
              [but_3e_thu, but_3e_fri],
              [but_ret_class_3, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)
