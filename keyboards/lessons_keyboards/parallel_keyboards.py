from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import LEXICON_RU

but_1_par = KeyboardButton(text='1')
but_2_par = KeyboardButton(text='2')
but_3_par = KeyboardButton(text='3')
but_4_par = KeyboardButton(text='4')
but_5_par = KeyboardButton(text='5')
but_6_par = KeyboardButton(text='6')
but_7_par = KeyboardButton(text='7')
but_8_par = KeyboardButton(text='8')
but_9_par = KeyboardButton(text='9')
but_10_par = KeyboardButton(text='10')
but_11_par = KeyboardButton(text='11')

par_key = ReplyKeyboardMarkup(
    keyboard=[[but_1_par, but_2_par, but_3_par, but_4_par],
              [but_5_par, but_6_par, but_7_par],
              [but_8_par, but_9_par],
              but_10_par, but_11_par],
    resize_keyboard=True
)

