from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


@router.message(F.text == '1А')
async def class_1a_command(m: Message):
    await m.answer(text=LEXICON_RU['1а'],
                   reply_markup=class_1a_key)


@router.message(F.text == '1Б')
async def class_1b_command(m: Message):
    await m.answer(text=LEXICON_RU['1б'],
                   reply_markup=class_1b_key)


@router.message(F.text == '1В')
async def class_1v_command(m: Message):
    await m.answer(text=LEXICON_RU['1в'],
                   reply_markup=class_1v_key)


@router.message(F.text == '2А')
async def class_2a_command(m: Message):
    await m.answer(text=LEXICON_RU['2а'],
                   reply_markup=class_2a_key)


@router.message(F.text == '2Б')
async def class_2b_command(m: Message):
    await m.answer(text=LEXICON_RU['2б'],
                   reply_markup=class_2b_key)


@router.message(F.text == '2В')
async def class_2v_command(m: Message):
    await m.answer(text=LEXICON_RU['2в'],
                   reply_markup=class_2v_key)


@router.message(F.text == '3А')
async def class_3a_command(m: Message):
    await m.answer(text=LEXICON_RU['3а'],
                   reply_markup=class_3a_key)


@router.message(F.text == '3Б')
async def class_3b_command(m: Message):
    await m.answer(text=LEXICON_RU['3б'],
                   reply_markup=class_3b_key)


@router.message(F.text == '3Э')
async def class_3e_command(m: Message):
    await m.answer(text=LEXICON_RU['3э'],
                   reply_markup=class_3e_key)


@router.message(F.text == '4А')
async def class_4a_command(m: Message):
    await m.answer(text=LEXICON_RU['4а'],
                   reply_markup=class_4a_key)


@router.message(F.text == '4Б')
async def class_4b_command(m: Message):
    await m.answer(text=LEXICON_RU['4б'],
                   reply_markup=class_4b_key)


@router.message(F.text == '4Э')
async def class_4e_command(m: Message):
    await m.answer(text=LEXICON_RU['4э'],
                   reply_markup=class_4e_key)


@router.message(F.text == '5А')
async def class_4a_command(m: Message):
    await m.answer(text=LEXICON_RU['5а'],
                   reply_markup=class_5a_key)


@router.message(F.text == '5А')
async def class_4a_command(m: Message):
    await m.answer(text=LEXICON_RU['5а'],
                   reply_markup=class_5a_key)


@router.message(F.text == '5А')
async def class_5a_command(m: Message):
    await m.answer(text=LEXICON_RU['5а'],
                   reply_markup=class_5a_key)


@router.message(F.text == '6А')
async def class_6a_command(m: Message):
    await m.answer(text=LEXICON_RU['6а'],
                   reply_markup=class_6a_key)


@router.message(F.text == '6А')
async def class_6a_command(m: Message):
    await m.answer(text=LEXICON_RU['6а'],
                   reply_markup=class_6a_key)


@router.message(F.text == '6А')
async def class_6a_command(m: Message):
    await m.answer(text=LEXICON_RU['6а'],
                   reply_markup=class_6a_key)


@router.message(F.text == '6А')
async def class_6a_command(m: Message):
    await m.answer(text=LEXICON_RU['6а'],
                   reply_markup=class_6a_key)


@router.message(F.text == '6А')
async def class_6a_command(m: Message):
    await m.answer(text=LEXICON_RU['6а'],
                   reply_markup=class_6a_key)


@router.message(F.text == '7А')
async def class_7a_command(m: Message):
    await m.answer(text=LEXICON_RU['7а'],
                   reply_markup=class_7a_key)


@router.message(F.text == '7А')
async def class_7a_command(m: Message):
    await m.answer(text=LEXICON_RU['7а'],
                   reply_markup=class_7a_key)


@router.message(F.text == '7А')
async def class_7a_command(m: Message):
    await m.answer(text=LEXICON_RU['7а'],
                   reply_markup=class_7a_key)


@router.message(F.text == '7А')
async def class_7a_command(m: Message):
    await m.answer(text=LEXICON_RU['7а'],
                   reply_markup=class_7a_key)


@router.message(F.text == '8А')
async def class_8a_command(m: Message):
    await m.answer(text=LEXICON_RU['8а'],
                   reply_markup=class_8a_key)


@router.message(F.text == '8А')
async def class_8a_command(m: Message):
    await m.answer(text=LEXICON_RU['8а'],
                   reply_markup=class_8a_key)


@router.message(F.text == '8А')
async def class_8a_command(m: Message):
    await m.answer(text=LEXICON_RU['8а'],
                   reply_markup=class_8a_key)


@router.message(F.text == '8А')
async def class_8a_command(m: Message):
    await m.answer(text=LEXICON_RU['8а'],
                   reply_markup=class_8a_key)


@router.message(F.text == '9А')
async def class_9a_command(m: Message):
    await m.answer(text=LEXICON_RU['9а'],
                   reply_markup=class_9a_key)


@router.message(F.text == '9А')
async def class_9a_command(m: Message):
    await m.answer(text=LEXICON_RU['9а'],
                   reply_markup=class_9a_key)


@router.message(F.text == '9А')
async def class_9a_command(m: Message):
    await m.answer(text=LEXICON_RU['9а'],
                   reply_markup=class_9a_key)


@router.message(F.text == '10А')
async def class_10a_command(m: Message):
    await m.answer(text=LEXICON_RU['10а'],
                   reply_markup=class_10a_key)


@router.message(F.text == '10А')
async def class_10a_command(m: Message):
    await m.answer(text=LEXICON_RU['10а'],
                   reply_markup=class_10a_key)


@router.message(F.text == '11А')
async def class_11a_command(m: Message):
    await m.answer(text=LEXICON_RU['11а'],
                   reply_markup=class_11a_key)


@router.message(F.text == '11А')
async def class_11a_command(m: Message):
    await m.answer(text=LEXICON_RU['11а'],
                   reply_markup=class_11a_key)


@router.message(F.text == '11А')
async def class_11a_command(m: Message):
    await m.answer(text=LEXICON_RU['11а'],
                   reply_markup=class_11a_key)
