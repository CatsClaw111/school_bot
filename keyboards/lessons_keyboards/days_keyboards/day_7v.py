from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_7, but_ret_par, but_ret_menu

but_7v_mon = KeyboardButton(text='Понедельник_7В')
but_7v_tue = KeyboardButton(text='Понедельник_7В')
but_7v_wed = KeyboardButton(text='Понедельник_7В')
but_7v_thu = KeyboardButton(text='Понедельник_7В')
but_7v_fri = KeyboardButton(text='Понедельник_7В')

days_7_key = ReplyKeyboardMarkup(
    keyboard=[[but_7v_mon, but_7v_tue, but_7v_wed],
              [but_7v_thu, but_7v_fri]
              [but_ret_class_7, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)