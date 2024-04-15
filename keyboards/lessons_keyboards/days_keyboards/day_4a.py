from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_4, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_4a_mon = KeyboardButton(text='Понедельник_4А')
but_4a_tue = KeyboardButton(text='Вторник_4А')
but_4a_wed = KeyboardButton(text='Среда_4А')
but_4a_thu = KeyboardButton(text='Четверг_4А')
but_4a_fri = KeyboardButton(text='Пятница_4А')

days_4a_key = ReplyKeyboardMarkup(
    keyboard=[[but_4a_mon, but_4a_tue, but_4a_wed],
              [but_4a_thu, but_4a_fri],
              [but_ret_class_4, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)
