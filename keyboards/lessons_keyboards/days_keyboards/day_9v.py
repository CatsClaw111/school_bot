from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.lessons_keyboards.class_keyboards import but_ret_class_9, but_ret_par, but_ret_menu

but_9v_mon = KeyboardButton(text='Понедельник_9В')
but_9v_tue = KeyboardButton(text='Вторник_9В')
but_9v_wed = KeyboardButton(text='Среда_9В')
but_9v_thu = KeyboardButton(text='Четверг_9В')
but_9v_fri = KeyboardButton(text='Пятница_9В')

days_9v_key = ReplyKeyboardMarkup(
    keyboard=[[but_9v_mon, but_9v_tue, but_9v_wed],
              [but_9v_thu, but_9v_fri],
              [but_ret_class_9, but_ret_par, but_ret_menu]],
    resize_keyboard=True
)