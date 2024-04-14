from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_1, but_ret_par, but_ret_menu

but_1v_mon = KeyboardButton(text='Понедельник_1В')
but_1v_tue = KeyboardButton(text='Понедельник_1В')
but_1v_wed = KeyboardButton(text='Понедельник_1В')
but_1v_thu = KeyboardButton(text='Понедельник_1В')
but_1v_fri = KeyboardButton(text='Понедельник_1В')

days_1_key = ReplyKeyboardMarkup(
    keyboard=[[but_1v_mon, but_1v_tue, but_1v_wed],
              [but_1v_thu, but_1v_fri]
              [but_ret_class_1, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)
