from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.start_keyboard import but_ret_menu

but_soc_tea = KeyboardButton(text='🗂Соц-эк')
but_gum_tea = KeyboardButton(text='🗣Гум')
but_gum_in_yaz_tea = KeyboardButton(text='🗣Гум ин.яз.')
but_tech_tea = KeyboardButton(text='💻Тех')
but_biohim_tea = KeyboardButton(text='🧪Ест-науч')
but_other_tea = KeyboardButton(text='📚Иные учителя')
but_other_ped = KeyboardButton(text='🖊Иной пед. персонал')
but_pri_tea = KeyboardButton(text='🧸Начальные классы')

tea_key = ReplyKeyboardMarkup(
    keyboard=[[but_gum_tea, but_gum_in_yaz_tea, but_soc_tea],
              [but_tech_tea, but_biohim_tea],
              [but_pri_tea, but_other_tea],
              [but_other_ped, but_ret_menu]],
    resize_keyboard=True
)