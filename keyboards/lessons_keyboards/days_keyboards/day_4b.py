from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_4, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_4b_mon = KeyboardButton(text='Понедельник_4Б')
but_4b_tue = KeyboardButton(text='Вторник_4Б')
but_4b_wed = KeyboardButton(text='Среда_4Б')
but_4b_thu = KeyboardButton(text='Четверг_4Б')
but_4b_fri = KeyboardButton(text='Пятница_4Б')

days_4b_key = ReplyKeyboardMarkup(
    keyboard=[[but_4b_mon, but_4b_tue, but_4b_wed],
              [but_4b_thu, but_4b_fri],
              [but_ret_class_4, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)