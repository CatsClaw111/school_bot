from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_6, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_6a_mon = KeyboardButton(text='Понедельник_6А')
but_6a_tue = KeyboardButton(text='Вторник_6А')
but_6a_wed = KeyboardButton(text='Среда_6А')
but_6a_thu = KeyboardButton(text='Четверг_6А')
but_6a_fri = KeyboardButton(text='Пятница_6А')

days_6a_key = ReplyKeyboardMarkup(
    keyboard=[[but_6a_mon, but_6a_tue, but_6a_wed],
              [but_6a_thu, but_6a_fri],
              [but_ret_class_6, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)