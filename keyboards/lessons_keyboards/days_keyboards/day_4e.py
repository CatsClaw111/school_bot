from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_4, but_ret_par, but_ret_menu

but_4e_mon = KeyboardButton(text='Понедельник_4Э')
but_4e_tue = KeyboardButton(text='Понедельник_4Э')
but_4e_wed = KeyboardButton(text='Понедельник_4Э')
but_4e_thu = KeyboardButton(text='Понедельник_4Э')
but_4e_fri = KeyboardButton(text='Понедельник_4Э')

days_4_key = ReplyKeyboardMarkup(
    keyboard=[[but_4e_mon, but_4e_tue, but_4e_wed],
              [but_4e_thu, but_4e_fri]
              [but_ret_class_4, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)