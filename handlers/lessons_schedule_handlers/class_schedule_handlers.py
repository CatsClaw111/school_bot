from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.lessons_keyboards.days_keyboards.day_1a import days_1a_key
from keyboards.lessons_keyboards.days_keyboards.day_1b import days_1b_key
from keyboards.lessons_keyboards.days_keyboards.day_1v import days_1v_key
from keyboards.lessons_keyboards.days_keyboards.day_2a import days_2a_key
from keyboards.lessons_keyboards.days_keyboards.day_2b import days_2b_key
from keyboards.lessons_keyboards.days_keyboards.day_2v import days_2v_key
from keyboards.lessons_keyboards.days_keyboards.day_3a import days_3a_key
from keyboards.lessons_keyboards.days_keyboards.day_3b import days_3b_key
from keyboards.lessons_keyboards.days_keyboards.day_3e import days_3e_key
from keyboards.lessons_keyboards.days_keyboards.day_4a import days_4a_key
from keyboards.lessons_keyboards.days_keyboards.day_4b import days_4b_key
from keyboards.lessons_keyboards.days_keyboards.day_4e import days_4e_key
from keyboards.lessons_keyboards.days_keyboards.day_5a import days_5a_key
from keyboards.lessons_keyboards.days_keyboards.day_5b import days_5b_key
from keyboards.lessons_keyboards.days_keyboards.day_5m import days_5m_key
from keyboards.lessons_keyboards.days_keyboards.day_6a import days_6a_key
from keyboards.lessons_keyboards.days_keyboards.day_6b import days_6b_key
from keyboards.lessons_keyboards.days_keyboards.day_6v import days_6v_key
from keyboards.lessons_keyboards.days_keyboards.day_6g import days_6g_key
from keyboards.lessons_keyboards.days_keyboards.day_6m import days_6m_key
from keyboards.lessons_keyboards.days_keyboards.day_7a import days_7a_key
from keyboards.lessons_keyboards.days_keyboards.day_7b import days_7b_key
from keyboards.lessons_keyboards.days_keyboards.day_7v import days_7v_key
from keyboards.lessons_keyboards.days_keyboards.day_7m import days_7m_key
from keyboards.lessons_keyboards.days_keyboards.day_8a import days_8a_key
from keyboards.lessons_keyboards.days_keyboards.day_8b import days_8b_key
from keyboards.lessons_keyboards.days_keyboards.day_8v import days_8v_key
from keyboards.lessons_keyboards.days_keyboards.day_8m import days_8m_key
from keyboards.lessons_keyboards.days_keyboards.day_9a import days_9a_key
from keyboards.lessons_keyboards.days_keyboards.day_9b import days_9b_key
from keyboards.lessons_keyboards.days_keyboards.day_9v import days_9v_key
from keyboards.lessons_keyboards.days_keyboards.day_10a import days_10a_key
from keyboards.lessons_keyboards.days_keyboards.day_10b import days_10b_key
from keyboards.lessons_keyboards.days_keyboards.day_11a import days_11a_key
from keyboards.lessons_keyboards.days_keyboards.day_11b import days_11b_key
from keyboards.lessons_keyboards.days_keyboards.day_11v import days_11v_key

router = Router()


@router.message(F.text == '1А')
async def class_1a_command(m: Message):
    await m.answer(text=LEXICON_RU['1а'],
                   reply_markup=days_1a_key)


@router.message(F.text == '1Б')
async def class_1b_command(m: Message):
    await m.answer(text=LEXICON_RU['1б'],
                   reply_markup=days_1b_key)


@router.message(F.text == '1В')
async def class_1v_command(m: Message):
    await m.answer(text=LEXICON_RU['1в'],
                   reply_markup=days_1v_key)


@router.message(F.text == '2А')
async def class_2a_command(m: Message):
    await m.answer(text=LEXICON_RU['2а'],
                   reply_markup=days_2a_key)


@router.message(F.text == '2Б')
async def class_2b_command(m: Message):
    await m.answer(text=LEXICON_RU['2б'],
                   reply_markup=days_2b_key)


@router.message(F.text == '2В')
async def class_2v_command(m: Message):
    await m.answer(text=LEXICON_RU['2в'],
                   reply_markup=days_2v_key)


@router.message(F.text == '3А')
async def class_3a_command(m: Message):
    await m.answer(text=LEXICON_RU['3а'],
                   reply_markup=days_3a_key)


@router.message(F.text == '3Б')
async def class_3b_command(m: Message):
    await m.answer(text=LEXICON_RU['3б'],
                   reply_markup=days_3b_key)


@router.message(F.text == '3Э')
async def class_3e_command(m: Message):
    await m.answer(text=LEXICON_RU['3э'],
                   reply_markup=days_3e_key)


@router.message(F.text == '4А')
async def class_4a_command(m: Message):
    await m.answer(text=LEXICON_RU['4а'],
                   reply_markup=days_4a_key)


@router.message(F.text == '4Б')
async def class_4b_command(m: Message):
    await m.answer(text=LEXICON_RU['4б'],
                   reply_markup=days_4b_key)


@router.message(F.text == '4Э')
async def class_4e_command(m: Message):
    await m.answer(text=LEXICON_RU['4э'],
                   reply_markup=days_4e_key)


@router.message(F.text == '5А')
async def class_5a_command(m: Message):
    await m.answer(text=LEXICON_RU['5а'],
                   reply_markup=days_5a_key)


@router.message(F.text == '5Б')
async def class_5b_command(m: Message):
    await m.answer(text=LEXICON_RU['5б'],
                   reply_markup=days_5b_key)


@router.message(F.text == '5М')
async def class_5m_command(m: Message):
    await m.answer(text=LEXICON_RU['5м'],
                   reply_markup=days_5m_key)


@router.message(F.text == '6А')
async def class_6a_command(m: Message):
    await m.answer(text=LEXICON_RU['6а'],
                   reply_markup=days_6a_key)


@router.message(F.text == '6Б')
async def class_6b_command(m: Message):
    await m.answer(text=LEXICON_RU['6б'],
                   reply_markup=days_6b_key)


@router.message(F.text == '6В')
async def class_6v_command(m: Message):
    await m.answer(text=LEXICON_RU['6в'],
                   reply_markup=days_6v_key)


@router.message(F.text == '6Г')
async def class_6g_command(m: Message):
    await m.answer(text=LEXICON_RU['6г'],
                   reply_markup=days_6g_key)


@router.message(F.text == '6М')
async def class_6m_command(m: Message):
    await m.answer(text=LEXICON_RU['6м'],
                   reply_markup=days_6m_key)


@router.message(F.text == '7А')
async def class_7a_command(m: Message):
    await m.answer(text=LEXICON_RU['7а'],
                   reply_markup=days_7a_key)


@router.message(F.text == '7Б')
async def class_7b_command(m: Message):
    await m.answer(text=LEXICON_RU['7б'],
                   reply_markup=days_7b_key)


@router.message(F.text == '7В')
async def class_7v_command(m: Message):
    await m.answer(text=LEXICON_RU['7в'],
                   reply_markup=days_7v_key)


@router.message(F.text == '7М')
async def class_7m_command(m: Message):
    await m.answer(text=LEXICON_RU['7м'],
                   reply_markup=days_7m_key)


@router.message(F.text == '8А')
async def class_8a_command(m: Message):
    await m.answer(text=LEXICON_RU['8а'],
                   reply_markup=days_8a_key)


@router.message(F.text == '8Б')
async def class_8b_command(m: Message):
    await m.answer(text=LEXICON_RU['8б'],
                   reply_markup=days_8b_key)


@router.message(F.text == '8В')
async def class_8v_command(m: Message):
    await m.answer(text=LEXICON_RU['8в'],
                   reply_markup=days_8v_key)


@router.message(F.text == '8М')
async def class_8m_command(m: Message):
    await m.answer(text=LEXICON_RU['8м'],
                   reply_markup=days_8m_key)


@router.message(F.text == '9А')
async def class_9a_command(m: Message):
    await m.answer(text=LEXICON_RU['9а'],
                   reply_markup=days_9a_key)


@router.message(F.text == '9Б')
async def class_9b_command(m: Message):
    await m.answer(text=LEXICON_RU['9б'],
                   reply_markup=days_9b_key)


@router.message(F.text == '9В')
async def class_9v_command(m: Message):
    await m.answer(text=LEXICON_RU['9в'],
                   reply_markup=days_9v_key)


@router.message(F.text == '10А')
async def class_10a_command(m: Message):
    await m.answer(text=LEXICON_RU['10а'],
                   reply_markup=days_10a_key)


@router.message(F.text == '10Б')
async def class_10b_command(m: Message):
    await m.answer(text=LEXICON_RU['10б'],
                   reply_markup=days_10b_key)


@router.message(F.text == '11А')
async def class_11a_command(m: Message):
    await m.answer(text=LEXICON_RU['11а'],
                   reply_markup=days_11a_key)


@router.message(F.text == '11Б')
async def class_11b_command(m: Message):
    await m.answer(text=LEXICON_RU['11б'],
                   reply_markup=days_11b_key)


@router.message(F.text == '11В')
async def class_11v_command(m: Message):
    await m.answer(text=LEXICON_RU['11в'],
                   reply_markup=days_11v_key)
