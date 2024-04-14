from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_9, but_ret_par, but_ret_menu

but_9b_mon = KeyboardButton(text='Понедельник_9Б')
but_9b_tue = KeyboardButton(text='Понедельник_9Б')
but_9b_wed = KeyboardButton(text='Понедельник_9Б')
but_9b_thu = KeyboardButton(text='Понедельник_9Б')
but_9b_fri = KeyboardButton(text='Понедельник_9Б')

days_9b_key = ReplyKeyboardMarkup(
    keyboard=[[but_9b_mon, but_9b_tue, but_9b_wed],
              [but_9b_thu, but_9b_fri],
              [but_ret_class_9, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)