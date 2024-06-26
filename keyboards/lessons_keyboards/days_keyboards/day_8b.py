from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_8, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_8b_mon = KeyboardButton(text='Понедельник_8Б')
but_8b_tue = KeyboardButton(text='Вторник_8Б')
but_8b_wed = KeyboardButton(text='Среда_8Б')
but_8b_thu = KeyboardButton(text='Четверг_8Б')
but_8b_fri = KeyboardButton(text='Пятница_8Б')

days_8b_key = ReplyKeyboardMarkup(
    keyboard=[[but_8b_mon, but_8b_tue, but_8b_wed],
              [but_8b_thu, but_8b_fri],
              [but_ret_class_8, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)