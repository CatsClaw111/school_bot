from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_8, but_ret_par, but_ret_menu

but_8m_mon = KeyboardButton(text='Понедельник_8М')
but_8m_tue = KeyboardButton(text='Понедельник_8М')
but_8m_wed = KeyboardButton(text='Понедельник_8М')
but_8m_thu = KeyboardButton(text='Понедельник_8М')
but_8m_fri = KeyboardButton(text='Понедельник_8М')

days_8_key = ReplyKeyboardMarkup(
    keyboard=[[but_8m_mon, but_8m_tue, but_8m_wed],
              [but_8m_thu, but_8m_fri]
              [but_ret_class_8, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)