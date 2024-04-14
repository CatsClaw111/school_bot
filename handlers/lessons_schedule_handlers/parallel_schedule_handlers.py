from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.lessons_keyboards.class_keyboards import class_1_key, class_2_key, class_3_key, class_4_key, class_5_key, \
    class_6_key, class_7_key, class_8_key, class_9_key, class_10_key, class_11_key
from keyboards.lessons_keyboards.parallel_keyboards import par_key
router = Router()


@router.message(F.text == '1')
async def par_1_command(m: Message):
    await m.answer(text=LEXICON_RU['1'],
                   reply_markup=class_1_key)
@router.message(F.text == 'К параллели 1-ых')
async def par1_1_command(m: Message):
    await m.answer(text=LEXICON_RU['1'],
                   reply_markup=class_1_key)



@router.message(F.text == '2')
async def par_2_command(m: Message):
    await m.answer(text=LEXICON_RU['2'],
                   reply_markup=class_2_key)
@router.message(F.text == 'К параллели 2-ых')
async def par1_2_command(m: Message):
    await m.answer(text=LEXICON_RU['2'],
                   reply_markup=class_2_key)


@router.message(F.text == '3')
async def par_3_command(m: Message):
    await m.answer(text=LEXICON_RU['3'],
                   reply_markup=class_3_key)
@router.message(F.text == 'К параллели 3-ых')
async def par1_3_command(m: Message):
    await m.answer(text=LEXICON_RU['3'],
                   reply_markup=class_3_key)


@router.message(F.text == '4')
async def par_4_command(m: Message):
    await m.answer(text=LEXICON_RU['4'],
                   reply_markup=class_4_key)
@router.message(F.text == 'К параллели 4-ых')
async def par1_4_command(m: Message):
    await m.answer(text=LEXICON_RU['4'],
                   reply_markup=class_4_key)


@router.message(F.text == '5')
async def par_5_command(m: Message):
    await m.answer(text=LEXICON_RU['5'],
                   reply_markup=class_5_key)
@router.message(F.text == 'К параллели 5-ых')
async def par1_5_command(m: Message):
    await m.answer(text=LEXICON_RU['5'],
                   reply_markup=class_5_key)


@router.message(F.text == '6')
async def par_6_command(m: Message):
    await m.answer(text=LEXICON_RU['6'],
                   reply_markup=class_6_key)
@router.message(F.text == 'К параллели 6-ых')
async def par1_6_command(m: Message):
    await m.answer(text=LEXICON_RU['6'],
                   reply_markup=class_6_key)


@router.message(F.text == '7')
async def par_7_command(m: Message):
    await m.answer(text=LEXICON_RU['7'],
                   reply_markup=class_7_key)
@router.message(F.text == 'К параллели 7-ых')
async def par1_7_command(m: Message):
    await m.answer(text=LEXICON_RU['7'],
                   reply_markup=class_7_key)


@router.message(F.text == '8')
async def par_8_command(m: Message):
    await m.answer(text=LEXICON_RU['8'],
                   reply_markup=class_8_key)
@router.message(F.text == 'К параллели 8-ых')
async def par1_8_command(m: Message):
    await m.answer(text=LEXICON_RU['8'],
                   reply_markup=class_8_key)


@router.message(F.text == '9')
async def par_9_command(m: Message):
    await m.answer(text=LEXICON_RU['9'],
                   reply_markup=class_9_key)
@router.message(F.text == 'К параллели 9-ых')
async def par1_9_command(m: Message):
    await m.answer(text=LEXICON_RU['9'],
                   reply_markup=class_9_key)


@router.message(F.text == '10')
async def par_10_command(m: Message):
    await m.answer(text=LEXICON_RU['10'],
                   reply_markup=class_10_key)
@router.message(F.text == 'К параллели 10-ых')
async def par1_10_command(m: Message):
    await m.answer(text=LEXICON_RU['10'],
                   reply_markup=class_10_key)


@router.message(F.text == '11')
async def par_11_command(m: Message):
    await m.answer(text=LEXICON_RU['11'],
                   reply_markup=class_11_key)
@router.message(F.text == 'К параллели 11-ых')
async def par1_11_command(m: Message):
    await m.answer(text=LEXICON_RU['11'],
                   reply_markup=class_11_key)


@router.message(F.text == 'К параллелям')
async def par_return_command(m: Message):
    await m.answer(text=LEXICON_RU['параллель'],
                   reply_markup=par_key)
