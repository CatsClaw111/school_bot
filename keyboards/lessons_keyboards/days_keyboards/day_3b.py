from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_3, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_3b_mon = KeyboardButton(text='Понедельник_3Б')
but_3b_tue = KeyboardButton(text='Вторник_3Б')
but_3b_wed = KeyboardButton(text='Среда_3Б')
but_3b_thu = KeyboardButton(text='Четверг_3Б')
but_3b_fri = KeyboardButton(text='Пятница_3Б')

days_3b_key = ReplyKeyboardMarkup(
    keyboard=[[but_3b_mon, but_3b_tue, but_3b_wed],
              [but_3b_thu, but_3b_fri],
              [but_ret_class_3, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)
