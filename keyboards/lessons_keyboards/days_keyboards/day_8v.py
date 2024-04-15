from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_8, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_8v_mon = KeyboardButton(text='Понедельник_8В')
but_8v_tue = KeyboardButton(text='Вторник_8В')
but_8v_wed = KeyboardButton(text='Среда_8В')
but_8v_thu = KeyboardButton(text='Четверг_8В')
but_8v_fri = KeyboardButton(text='Пятница_8В')

days_8v_key = ReplyKeyboardMarkup(
    keyboard=[[but_8v_mon, but_8v_tue, but_8v_wed],
              [but_8v_thu, but_8v_fri],
              [but_ret_class_8, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)