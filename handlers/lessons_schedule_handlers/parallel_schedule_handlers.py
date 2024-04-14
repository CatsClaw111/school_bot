from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


@router.message(F.text == '1')
async def par_1_command(m: Message):
    await m.answer(text=LEXICON_RU['1'],
                   reply_markup=par_1)


@router.message(F.text == '2')
async def par_2_command(m: Message):
    await m.answer(text=LEXICON_RU['2'],
                   reply_markup=par_2_key)


@router.message(F.text == '3')
async def par_3_command(m: Message):
    await m.answer(text=LEXICON_RU['3'],
                   reply_markup=par_3_key)


@router.message(F.text == '4')
async def par_4_command(m: Message):
    await m.answer(text=LEXICON_RU['4'],
                   reply_markup=par_4_key)


@router.message(F.text == '5')
async def par_5_command(m: Message):
    await m.answer(text=LEXICON_RU['5'],
                   reply_markup=par_5_key)


@router.message(F.text == '6')
async def par_6_command(m: Message):
    await m.answer(text=LEXICON_RU['6'],
                   reply_markup=par_6_key)


@router.message(F.text == '7')
async def par_7_command(m: Message):
    await m.answer(text=LEXICON_RU['7'],
                   reply_markup=par_7_key)


@router.message(F.text == '8')
async def par_8_command(m: Message):
    await m.answer(text=LEXICON_RU['8'],
                   reply_markup=par_8_key)


@router.message(F.text == '9')
async def par_9_command(m: Message):
    await m.answer(text=LEXICON_RU['9'],
                   reply_markup=par_9_key)


@router.message(F.text == '10')
async def par_10_command(m: Message):
    await m.answer(text=LEXICON_RU['10'],
                   reply_markup=par_10_key)


@router.message(F.text == '11')
async def par_11_command(m: Message):
    await m.answer(text=LEXICON_RU['11'],
                   reply_markup=par_11_key)
