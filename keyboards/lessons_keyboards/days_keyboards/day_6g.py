from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_6, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_6g_mon = KeyboardButton(text='Понедельник_6Г')
but_6g_tue = KeyboardButton(text='Вторник_6Г')
but_6g_wed = KeyboardButton(text='Среда_6Г')
but_6g_thu = KeyboardButton(text='Четверг_6Г')
but_6g_fri = KeyboardButton(text='Пятница_6Г')

days_6g_key = ReplyKeyboardMarkup(
    keyboard=[[but_6g_mon, but_6g_tue, but_6g_wed],
              [but_6g_thu, but_6g_fri],
              [but_ret_class_6, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)