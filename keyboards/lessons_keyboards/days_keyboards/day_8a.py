from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_8, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_8a_mon = KeyboardButton(text='Понедельник_8А')
but_8a_tue = KeyboardButton(text='Вторник_8А')
but_8a_wed = KeyboardButton(text='Среда_8А')
but_8a_thu = KeyboardButton(text='Четверг_8А')
but_8a_fri = KeyboardButton(text='Пятница_8А')

days_8a_key = ReplyKeyboardMarkup(
    keyboard=[[but_8a_mon, but_8a_tue, but_8a_wed],
              [but_8a_thu, but_8a_fri],
              [but_ret_class_8, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)