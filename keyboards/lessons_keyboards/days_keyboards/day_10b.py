from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_10, but_ret_par, but_ret_menu

but_10b_mon = KeyboardButton(text='Понедельник_10Б')
but_10b_tue = KeyboardButton(text='Вторник_10Б')
but_10b_wed = KeyboardButton(text='Среда_10Б')
but_10b_thu = KeyboardButton(text='Четверг_10Б')
but_10b_fri = KeyboardButton(text='Пятница_10Б')

days_10b_key = ReplyKeyboardMarkup(
    keyboard=[[but_10b_mon, but_10b_tue, but_10b_wed],
              [but_10b_thu, but_10b_fri],
              [but_ret_class_10, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)