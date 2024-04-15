from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.start_keyboard import but_ret_menu

but_ret_par = KeyboardButton(text='🗒К параллелям')
but_ret_class_1 = KeyboardButton(text='👶К 1-ым')
but_ret_class_2 = KeyboardButton(text='👶К 2-ым')
but_ret_class_3 = KeyboardButton(text='👶К 3-ым')
but_ret_class_4 = KeyboardButton(text='👶К 4-ым')
but_ret_class_5 = KeyboardButton(text='👦🏻К 5-ым👧🏻')
but_ret_class_6 = KeyboardButton(text='👦🏻К 6-ым👧🏻')
but_ret_class_7 = KeyboardButton(text='👦🏻К 7-ым👧🏻')
but_ret_class_8 = KeyboardButton(text='👨🏻К 8-ым👩🏻')
but_ret_class_9 = KeyboardButton(text='👨🏻К 9-ым👩🏻')
but_ret_class_10 = KeyboardButton(text='👴🏻К 10-ым👵🏻')
but_ret_class_11 = KeyboardButton(text='👴🏻К 11-ым👵🏻')

#############################################################

but_1a = KeyboardButton(text='1А')
but_1b = KeyboardButton(text='1Б')
but_1v = KeyboardButton(text='1В')

class_1_key = ReplyKeyboardMarkup(
    keyboard=[[but_1a, but_1b, but_1v],
              [but_ret_par, but_ret_menu]],
    resize_keyboard=True
)

but_2a = KeyboardButton(text='2А')
but_2b = KeyboardButton(text='2Б')
but_2v = KeyboardButton(text='2В')

class_2_key = ReplyKeyboardMarkup(
    keyboard=[[but_2a, but_2b, but_2v],
              [but_ret_par, but_ret_menu]],
    resize_keyboard=True
)

but_3a = KeyboardButton(text='3А')
but_3b = KeyboardButton(text='3Б')
but_3e = KeyboardButton(text='3Э')

class_3_key = ReplyKeyboardMarkup(
    keyboard=[[but_3a, but_3b, but_3e],
              [but_ret_par, but_ret_menu]],
    resize_keyboard=True
)

but_4a = KeyboardButton(text='4А')
but_4b = KeyboardButton(text='4Б')
but_4e = KeyboardButton(text='4Э')

class_4_key = ReplyKeyboardMarkup(
    keyboard=[[but_4a, but_4b, but_4e],
              [but_ret_par, but_ret_menu]],
    resize_keyboard=True
)

but_5a = KeyboardButton(text='5А')
but_5b = KeyboardButton(text='5Б')
but_5m = KeyboardButton(text='5М')

class_5_key = ReplyKeyboardMarkup(
    keyboard=[[but_5a, but_5b, but_5m],
              [but_ret_par, but_ret_menu]],
    resize_keyboard=True
)

but_6a = KeyboardButton(text='6А')
but_6b = KeyboardButton(text='6Б')
but_6v = KeyboardButton(text='6В')
but_6g = KeyboardButton(text='6Г')
but_6m = KeyboardButton(text='6М')

class_6_key = ReplyKeyboardMarkup(
    keyboard=[[but_6a, but_6b, but_6v],
              [but_6g, but_6m],
              [but_ret_par, but_ret_menu]],
    resize_keyboard=True
)

but_7a = KeyboardButton(text='7А')
but_7b = KeyboardButton(text='7Б')
but_7v = KeyboardButton(text='7В')
but_7m = KeyboardButton(text='7М')

class_7_key = ReplyKeyboardMarkup(
    keyboard=[[but_7a, but_7b],
              [but_7v, but_7m],
              [but_ret_par, but_ret_menu]],
    resize_keyboard=True
)

but_8a = KeyboardButton(text='8А')
but_8b = KeyboardButton(text='8Б')
but_8v = KeyboardButton(text='8В')
but_8m = KeyboardButton(text='8М')

class_8_key = ReplyKeyboardMarkup(
    keyboard=[[but_8a, but_8b],
              [but_8v, but_8m],
              [but_ret_par, but_ret_menu]],
    resize_keyboard=True
)

but_9a = KeyboardButton(text='9А')
but_9b = KeyboardButton(text='9Б')
but_9v = KeyboardButton(text='9В')

class_9_key = ReplyKeyboardMarkup(
    keyboard=[[but_9a, but_9b, but_9v],
              [but_ret_par, but_ret_menu]],
    resize_keyboard=True
)

but_10a = KeyboardButton(text='10А')
but_10b = KeyboardButton(text='10Б')

class_10_key = ReplyKeyboardMarkup(
    keyboard=[[but_10a, but_10b],
              [but_ret_par, but_ret_menu]],
    resize_keyboard=True
)

but_11a = KeyboardButton(text='11А')
but_11b = KeyboardButton(text='11Б')
but_11v = KeyboardButton(text='11В')

class_11_key = ReplyKeyboardMarkup(
    keyboard=[[but_11a, but_11b, but_11v],
              [but_ret_par, but_ret_menu]],
    resize_keyboard=True
)