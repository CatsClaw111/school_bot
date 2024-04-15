from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

but_ret_menu = KeyboardButton(text='📋В главное меню')

but_les_sche = KeyboardButton(text='🗓Расписание уроков')
but_bre_sche = KeyboardButton(text='🛎️Расписание звонков')
but_teach = KeyboardButton(text='👨‍🏫Учителя👩‍🏫')
but_cont = KeyboardButton(text='🗄Контакты')
but_gro = KeyboardButton(text='🌐Группы школы')

start_key = ReplyKeyboardMarkup(
    keyboard=[[but_les_sche, but_teach, but_bre_sche],
              [but_gro, but_cont]],
    resize_keyboard=True
)