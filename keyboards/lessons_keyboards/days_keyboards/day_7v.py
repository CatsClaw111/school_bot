from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_7, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_7v_mon = KeyboardButton(text='Понедельник_7В')
but_7v_tue = KeyboardButton(text='Вторник_7В')
but_7v_wed = KeyboardButton(text='Среда_7В')
but_7v_thu = KeyboardButton(text='Четверг_7В')
but_7v_fri = KeyboardButton(text='Пятница_7В')

days_7v_key = ReplyKeyboardMarkup(
    keyboard=[[but_7v_mon, but_7v_tue, but_7v_wed],
              [but_7v_thu, but_7v_fri],
              [but_ret_class_7, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)