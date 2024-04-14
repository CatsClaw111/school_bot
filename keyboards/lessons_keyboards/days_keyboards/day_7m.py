from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_7, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_7m_mon = KeyboardButton(text='Понедельник_7М')
but_7m_tue = KeyboardButton(text='Понедельник_7М')
but_7m_wed = KeyboardButton(text='Понедельник_7М')
but_7m_thu = KeyboardButton(text='Понедельник_7М')
but_7m_fri = KeyboardButton(text='Понедельник_7М')

days_7m_key = ReplyKeyboardMarkup(
    keyboard=[[but_7m_mon, but_7m_tue, but_7m_wed],
              [but_7m_thu, but_7m_fri]
              [but_ret_class_7, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)