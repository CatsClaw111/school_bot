from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_6, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_6v_mon = KeyboardButton(text='Понедельник_6В')
but_6v_tue = KeyboardButton(text='Вторник_6В')
but_6v_wed = KeyboardButton(text='Среда_6В')
but_6v_thu = KeyboardButton(text='Четверг_6В')
but_6v_fri = KeyboardButton(text='Пятница_6В')

days_6v_key = ReplyKeyboardMarkup(
    keyboard=[[but_6v_mon, but_6v_tue, but_6v_wed],
              [but_6v_thu, but_6v_fri],
              [but_ret_class_6, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)