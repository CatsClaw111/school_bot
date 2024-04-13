from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import LEXICON_RU

but_gen_bre_sche = KeyboardButton(text='Общее')
but_prim_bre_sche = KeyboardButton(text='Начальная школа')


break_key = ReplyKeyboardMarkup(
    keyboard=[[but_gen_bre_sche, but_prim_bre_sche]],
    resize_keyboard=True
)