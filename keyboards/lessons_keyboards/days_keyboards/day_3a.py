from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_3, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_3a_mon = KeyboardButton(text='Понедельник_3А')
but_3a_tue = KeyboardButton(text='Вторник_3А')
but_3a_wed = KeyboardButton(text='Среда_3А')
but_3a_thu = KeyboardButton(text='Четверг_3А')
but_3a_fri = KeyboardButton(text='Пятница_3А')

days_3a_key = ReplyKeyboardMarkup(
    keyboard=[[but_3a_mon, but_3a_tue, but_3a_wed],
              [but_3a_thu, but_3a_fri],
              [but_ret_class_3, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)
