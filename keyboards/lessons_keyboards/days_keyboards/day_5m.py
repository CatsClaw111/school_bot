from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_5, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_5m_mon = KeyboardButton(text='Понедельник_5М')
but_5m_tue = KeyboardButton(text='Понедельник_5М')
but_5m_wed = KeyboardButton(text='Понедельник_5М')
but_5m_thu = KeyboardButton(text='Понедельник_5М')
but_5m_fri = KeyboardButton(text='Понедельник_5М')

days_5m_key = ReplyKeyboardMarkup(
    keyboard=[[but_5m_mon, but_5m_tue, but_5m_wed],
              [but_5m_thu, but_5m_fri]
              [but_ret_class_5, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)