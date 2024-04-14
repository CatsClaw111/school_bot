from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_2, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_2v_mon = KeyboardButton(text='Понедельник_2В')
but_2v_tue = KeyboardButton(text='Понедельник_2В')
but_2v_wed = KeyboardButton(text='Понедельник_2В')
but_2v_thu = KeyboardButton(text='Понедельник_2В')
but_2v_fri = KeyboardButton(text='Понедельник_2В')

days_2v_key = ReplyKeyboardMarkup(
    keyboard=[[but_2v_mon, but_2v_tue, but_2v_wed],
              [but_2v_thu, but_2v_fri]
              [but_ret_class_2, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)
