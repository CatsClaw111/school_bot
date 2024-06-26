from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_6, but_ret_par
from keyboards.start_keyboard import but_ret_menu

but_6m_mon = KeyboardButton(text='Понедельник_6М')
but_6m_tue = KeyboardButton(text='Вторник_6М')
but_6m_wed = KeyboardButton(text='Среда_6М')
but_6m_thu = KeyboardButton(text='Четверг_6М')
but_6m_fri = KeyboardButton(text='Пятница_6М')

days_6m_key = ReplyKeyboardMarkup(
    keyboard=[[but_6m_mon, but_6m_tue, but_6m_wed],
              [but_6m_thu, but_6m_fri],
              [but_ret_class_6, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)