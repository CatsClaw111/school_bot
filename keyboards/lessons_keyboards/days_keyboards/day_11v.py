from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_11, but_ret_par, but_ret_menu

but_11v_mon = KeyboardButton(text='Понедельник_11В')
but_11v_tue = KeyboardButton(text='Вторник_11В')
but_11v_wed = KeyboardButton(text='Среда_11В')
but_11v_thu = KeyboardButton(text='Четверг_11В')
but_11v_fri = KeyboardButton(text='Пятница_11В')

days_11v_key = ReplyKeyboardMarkup(
    keyboard=[[but_11v_mon, but_11v_tue, but_11v_wed],
              [but_11v_thu, but_11v_fri],
              [but_ret_class_11, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)