from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_1, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_1a_mon = KeyboardButton(text='Понедельник_1А')
but_1a_tue = KeyboardButton(text='Вторник_1А')
but_1a_wed = KeyboardButton(text='Среда_1А')
but_1a_thu = KeyboardButton(text='Четверг_1А')
but_1a_fri = KeyboardButton(text='Пятница_1А')

days_1a_key = ReplyKeyboardMarkup(
    keyboard=[[but_1a_mon, but_1a_tue, but_1a_wed],
              [but_1a_thu, but_1a_fri],
              [but_ret_class_1, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)
