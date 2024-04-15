from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.start_keyboard import but_ret_menu


but_gen_bre_sche = KeyboardButton(text='👨🏻Общее👩🏻')
but_prim_bre_sche = KeyboardButton(text='👶Начальная школа')


break_key = ReplyKeyboardMarkup(
    keyboard=[[but_gen_bre_sche, but_prim_bre_sche],
              [but_ret_menu]],
    resize_keyboard=True
)