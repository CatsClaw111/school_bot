from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_11, but_ret_par, but_ret_menu

but_11b_mon = KeyboardButton(text='Понедельник_11Б')
but_11b_tue = KeyboardButton(text='Вторник_11Б')
but_11b_wed = KeyboardButton(text='Среда_11Б')
but_11b_thu = KeyboardButton(text='Четверг_11Б')
but_11b_fri = KeyboardButton(text='Пятница_11Б')

days_11b_key = ReplyKeyboardMarkup(
    keyboard=[[but_11b_mon, but_11b_tue, but_11b_wed],
              [but_11b_thu, but_11b_fri],
              [but_ret_class_11, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)