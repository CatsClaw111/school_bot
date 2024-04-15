from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.start_keyboard import but_ret_menu

but_soc_tea = KeyboardButton(text='Соц-эк направленность')
but_gum_tea = KeyboardButton(text='Гум направленность')
but_tech_tea = KeyboardButton(text='Тех направленность')
but_biohim_tea = KeyboardButton(text='Ест-науч направленность')

tea_key = ReplyKeyboardMarkup(
    keyboard=[[but_gum_tea, but_soc_tea],
              [but_tech_tea, but_biohim_tea],
              [but_ret_menu]],
    resize_keyboard=True
)