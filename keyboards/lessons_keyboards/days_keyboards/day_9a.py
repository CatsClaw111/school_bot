from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_9, but_ret_par, but_ret_menu

but_9a_mon = KeyboardButton(text='Понедельник_9А')
but_9a_tue = KeyboardButton(text='Понедельник_9А')
but_9a_wed = KeyboardButton(text='Понедельник_9А')
but_9a_thu = KeyboardButton(text='Понедельник_9А')
but_9a_fri = KeyboardButton(text='Понедельник_9А')

days_9a_key = ReplyKeyboardMarkup(
    keyboard=[[but_9a_mon, but_9a_tue, but_9a_wed],
              [but_9a_thu, but_9a_fri],
              [but_ret_class_9, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)