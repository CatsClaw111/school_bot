from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


@router.message(F.text == 'Понедельник_1А')
async def monday_1a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_1а'])


@router.message(F.text == 'Вторник_1А')
async def tuesday_1a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_1а'])


@router.message(F.text == 'Среда_1А')
async def wednesday_1a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_1а'])


@router.message(F.text == 'Четверг_1А')
async def thursday_1a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_1а'])


@router.message(F.text == 'Пятница_1А')
async def friday_1a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_1а'])


@router.message(F.text == 'Понедельник_1Б')
async def monday_1b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_1б'])


@router.message(F.text == 'Вторник_1Б')
async def tuesday_1b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_1б'])


@router.message(F.text == 'Среда_1Б')
async def wednesday_1b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_1б'])


@router.message(F.text == 'Четверг_1Б')
async def thursday_1b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_1б'])


@router.message(F.text == 'Пятница_1Б')
async def friday_1b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_1б'])


@router.message(F.text == 'Понедельник_1В')
async def monday_1v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_1в'])


@router.message(F.text == 'Вторник_1В')
async def tuesday_1v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_1в'])


@router.message(F.text == 'Среда_1В')
async def wednesday_1v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_1в'])


@router.message(F.text == 'Четверг_1В')
async def thursday_1v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_1в'])


@router.message(F.text == 'Пятница_1В')
async def friday_1v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_1в'])


@router.message(F.text == 'Понедельник_2А')
async def monday_2a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_2а'])


@router.message(F.text == 'Вторник_2А')
async def tuesday_2a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_2а'])


@router.message(F.text == 'Среда_2А')
async def wednesday_2a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_2а'])


@router.message(F.text == 'Четверг_2А')
async def thursday_2a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_2а'])


@router.message(F.text == 'Пятница_2А')
async def friday_2a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_2а'])


@router.message(F.text == 'Понедельник_2Б')
async def monday_2b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_2б'])


@router.message(F.text == 'Вторник_2Б')
async def tuesday_2b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_2б'])


@router.message(F.text == 'Среда_2Б')
async def wednesday_2b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_2б'])


@router.message(F.text == 'Четверг_2Б')
async def thursday_2b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_2б'])


@router.message(F.text == 'Пятница_2Б')
async def friday_2b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_2б'])


@router.message(F.text == 'Понедельник_2В')
async def monday_2v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_2в'])


@router.message(F.text == 'Вторник_2В')
async def tuesday_2v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_2в'])


@router.message(F.text == 'Среда_2В')
async def wednesday_2v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_2в'])


@router.message(F.text == 'Четверг_2В')
async def thursday_2v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_2в'])


@router.message(F.text == 'Пятница_2В')
async def friday_2v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_2в'])


@router.message(F.text == 'Понедельник_3А')
async def monday_3a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_3а'])


@router.message(F.text == 'Вторник_3А')
async def tuesday_3a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_3а'])


@router.message(F.text == 'Среда_3А')
async def wednesday_3a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_3а'])


@router.message(F.text == 'Четверг_3А')
async def thursday_3a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_3а'])


@router.message(F.text == 'Пятница_3А')
async def friday_3a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_3а'])


@router.message(F.text == 'Понедельник_3Б')
async def monday_3b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_3б'])


@router.message(F.text == 'Вторник_3Б')
async def tuesday_3b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_3б'])


@router.message(F.text == 'Среда_3Б')
async def wednesday_3b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_3б'])


@router.message(F.text == 'Четверг_3Б')
async def thursday_3b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_3б'])


@router.message(F.text == 'Пятница_3Б')
async def friday_3b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_3б'])


@router.message(F.text == 'Понедельник_3Э')
async def monday_3e_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_3э'])


@router.message(F.text == 'Вторник_3Э')
async def tuesday_3e_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_3э'])


@router.message(F.text == 'Среда_3Э')
async def wednesday_3e_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_3э'])


@router.message(F.text == 'Четверг_3Э')
async def thursday_3e_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_3э'])


@router.message(F.text == 'Пятница_3Э')
async def friday_3e_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_3э'])


@router.message(F.text == 'Понедельник_4А')
async def monday_4a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_4а'])


@router.message(F.text == 'Вторник_4А')
async def tuesday_4a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_4а'])


@router.message(F.text == 'Среда_4А')
async def wednesday_4a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_4а'])


@router.message(F.text == 'Четверг_4А')
async def thursday_4a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_4а'])


@router.message(F.text == 'Пятница_4А')
async def friday_4a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_4а'])


@router.message(F.text == 'Понедельник_4Б')
async def monday_4b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_4б'])


@router.message(F.text == 'Вторник_4Б')
async def tuesday_4b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_4б'])


@router.message(F.text == 'Среда_4Б')
async def wednesday_4b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_4б'])


@router.message(F.text == 'Четверг_4Б')
async def thursday_4b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_4б'])


@router.message(F.text == 'Пятница_4Б')
async def friday_4b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_4б'])


@router.message(F.text == 'Понедельник_4Э')
async def monday_4e_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_4э'])


@router.message(F.text == 'Вторник_4Э')
async def tuesday_4e_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_4э'])


@router.message(F.text == 'Среда_4Э')
async def wednesday_4e_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_4э'])


@router.message(F.text == 'Четверг_4Э')
async def thursday_4e_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_4э'])


@router.message(F.text == 'Пятница_4Э')
async def friday_4e_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_4э'])


@router.message(F.text == 'Понедельник_5А')
async def monday_5a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_5а'])


@router.message(F.text == 'Вторник_5А')
async def tuesday_5a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_5а'])


@router.message(F.text == 'Среда_5А')
async def wednesday_5a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_5а'])


@router.message(F.text == 'Четверг_5А')
async def thursday_5a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_5а'])


@router.message(F.text == 'Пятница_5А')
async def friday_5a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_5а'])


@router.message(F.text == 'Понедельник_5Б')
async def monday_5b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_5б'])


@router.message(F.text == 'Вторник_5Б')
async def tuesday_5b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_5б'])


@router.message(F.text == 'Среда_5Б')
async def wednesday_5b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_5б'])


@router.message(F.text == 'Четверг_5Б')
async def thursday_5b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_5б'])


@router.message(F.text == 'Пятница_5Б')
async def friday_5b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_5б'])


@router.message(F.text == 'Понедельник_5М')
async def monday_5m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_5м'])


@router.message(F.text == 'Вторник_5М')
async def tuesday_5m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_5м'])


@router.message(F.text == 'Среда_5М')
async def wednesday_5m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_5м'])


@router.message(F.text == 'Четверг_5М')
async def thursday_5m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_5м'])


@router.message(F.text == 'Пятница_5М')
async def friday_5m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_5м'])


@router.message(F.text == 'Понедельник_6А')
async def monday_6a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_6а'])


@router.message(F.text == 'Вторник_6А')
async def tuesday_6a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_6а'])


@router.message(F.text == 'Среда_6А')
async def wednesday_6a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_6а'])


@router.message(F.text == 'Четверг_6А')
async def thursday_6a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_6а'])


@router.message(F.text == 'Пятница_6А')
async def friday_6a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_6а'])


@router.message(F.text == 'Понедельник_6Б')
async def monday_6b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_6б'])


@router.message(F.text == 'Вторник_6Б')
async def tuesday_6b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_6б'])


@router.message(F.text == 'Среда_6Б')
async def wednesday_6b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_6б'])


@router.message(F.text == 'Четверг_6Б')
async def thursday_6b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_6б'])


@router.message(F.text == 'Пятница_6Б')
async def friday_6b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_6б'])


@router.message(F.text == 'Понедельник_6В')
async def monday_6v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_6в'])


@router.message(F.text == 'Вторник_6В')
async def tuesday_6v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_6в'])


@router.message(F.text == 'Среда_6В')
async def wednesday_6v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_6в'])


@router.message(F.text == 'Четверг_6В')
async def thursday_6v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_6в'])


@router.message(F.text == 'Пятница_6В')
async def friday_6v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_6в'])


@router.message(F.text == 'Понедельник_6Г')
async def monday_6g_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_6г'])


@router.message(F.text == 'Вторник_6Г')
async def tuesday_6g_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_6г'])


@router.message(F.text == 'Среда_6Г')
async def wednesday_6g_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_6г'])


@router.message(F.text == 'Четверг_6Г')
async def thursday_6g_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_6г'])


@router.message(F.text == 'Пятница_6Г')
async def friday_6g_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_6г'])


@router.message(F.text == 'Понедельник_6М')
async def monday_6m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_6м'])


@router.message(F.text == 'Вторник_6М')
async def tuesday_6m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_6м'])


@router.message(F.text == 'Среда_6М')
async def wednesday_6m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_6м'])


@router.message(F.text == 'Четверг_6М')
async def thursday_6m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_6м'])


@router.message(F.text == 'Пятница_6М')
async def friday_6m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_6м'])


@router.message(F.text == 'Понедельник_7А')
async def monday_7a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_7а'])


@router.message(F.text == 'Вторник_7А')
async def tuesday_7a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_7а'])


@router.message(F.text == 'Среда_7А')
async def wednesday_7a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_7а'])


@router.message(F.text == 'Четверг_7А')
async def thursday_7a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_7а'])


@router.message(F.text == 'Пятница_7А')
async def friday_7a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_7а'])


@router.message(F.text == 'Понедельник_7Б')
async def monday_7b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_7б'])


@router.message(F.text == 'Вторник_7Б')
async def tuesday_7b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_7б'])


@router.message(F.text == 'Среда_7Б')
async def wednesday_7b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_7б'])


@router.message(F.text == 'Четверг_7Б')
async def thursday_7b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_7б'])


@router.message(F.text == 'Пятница_7Б')
async def friday_7b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_7б'])


@router.message(F.text == 'Понедельник_7В')
async def monday_7v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_7в'])


@router.message(F.text == 'Вторник_7В')
async def tuesday_7v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_7в'])


@router.message(F.text == 'Среда_7В')
async def wednesday_7v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_7в'])


@router.message(F.text == 'Четверг_7В')
async def thursday_7v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_7в'])


@router.message(F.text == 'Пятница_7В')
async def friday_7v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_7в'])


@router.message(F.text == 'Понедельник_7М')
async def monday_7m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_7м'])


@router.message(F.text == 'Вторник_7М')
async def tuesday_7m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_7м'])


@router.message(F.text == 'Среда_7М')
async def wednesday_7m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_7м'])


@router.message(F.text == 'Четверг_7М')
async def thursday_7m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_7м'])


@router.message(F.text == 'Пятница_7М')
async def friday_7m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_7м'])


@router.message(F.text == 'Понедельник_8А')
async def monday_8a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_8а'])


@router.message(F.text == 'Вторник_8А')
async def tuesday_8a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_8а'])


@router.message(F.text == 'Среда_8А')
async def wednesday_8a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_8а'])


@router.message(F.text == 'Четверг_8А')
async def thursday_8a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_8а'])


@router.message(F.text == 'Пятница_8А')
async def friday_8a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_8а'])


@router.message(F.text == 'Понедельник_8Б')
async def monday_8b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_8б'])


@router.message(F.text == 'Вторник_8Б')
async def tuesday_8b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_8б'])


@router.message(F.text == 'Среда_8Б')
async def wednesday_8b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_8б'])


@router.message(F.text == 'Четверг_8Б')
async def thursday_8b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_8б'])


@router.message(F.text == 'Пятница_8Б')
async def friday_8b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_8б'])


@router.message(F.text == 'Понедельник_8В')
async def monday_8v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_8в'])


@router.message(F.text == 'Вторник_8В')
async def tuesday_8v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_8в'])


@router.message(F.text == 'Среда_8В')
async def wednesday_8v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_8в'])


@router.message(F.text == 'Четверг_8В')
async def thursday_8v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_8в'])


@router.message(F.text == 'Пятница_8В')
async def friday_8v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_8в'])


@router.message(F.text == 'Понедельник_8М')
async def monday_8m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_8м'])


@router.message(F.text == 'Вторник_8М')
async def tuesday_8m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_8м'])


@router.message(F.text == 'Среда_8М')
async def wednesday_8m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_8м'])


@router.message(F.text == 'Четверг_8М')
async def thursday_8m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_8м'])


@router.message(F.text == 'Пятница_8М')
async def friday_8m_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_8м'])


@router.message(F.text == 'Понедельник_9А')
async def monday_9a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_9а'])


@router.message(F.text == 'Вторник_9А')
async def tuesday_9a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_9а'])


@router.message(F.text == 'Среда_9А')
async def wednesday_9a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_9а'])


@router.message(F.text == 'Четверг_9А')
async def thursday_9a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_9а'])


@router.message(F.text == 'Пятница_9А')
async def friday_9a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_9а'])


@router.message(F.text == 'Понедельник_9Б')
async def monday_9b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_9б'])


@router.message(F.text == 'Вторник_9Б')
async def tuesday_9b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_9б'])


@router.message(F.text == 'Среда_9Б')
async def wednesday_9b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_9б'])


@router.message(F.text == 'Четверг_9Б')
async def thursday_9b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_9б'])


@router.message(F.text == 'Пятница_9Б')
async def friday_9b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_9б'])


@router.message(F.text == 'Понедельник_9В')
async def monday_9v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_9в'])


@router.message(F.text == 'Вторник_9В')
async def tuesday_9v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_9в'])


@router.message(F.text == 'Среда_9В')
async def wednesday_9v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_9в'])


@router.message(F.text == 'Четверг_9В')
async def thursday_9v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_9в'])


@router.message(F.text == 'Пятница_9В')
async def friday_9v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_9в'])


@router.message(F.text == 'Понедельник_10А')
async def monday_10a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_10а'])


@router.message(F.text == 'Вторник_10А')
async def tuesday_10a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_10а'])


@router.message(F.text == 'Среда_10А')
async def wednesday_10a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_10а'])


@router.message(F.text == 'Четверг_10А')
async def thursday_10a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_10а'])


@router.message(F.text == 'Пятница_10А')
async def friday_10a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_10а'])


@router.message(F.text == 'Понедельник_10Б')
async def monday_10b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_10б'])


@router.message(F.text == 'Вторник_10Б')
async def tuesday_10b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_10б'])


@router.message(F.text == 'Среда_10Б')
async def wednesday_10b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_10б'])


@router.message(F.text == 'Четверг_10Б')
async def thursday_10b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_10б'])


@router.message(F.text == 'Пятница_10Б')
async def friday_10b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_10б'])


@router.message(F.text == 'Понедельник_11А')
async def monday_11a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_11а'])


@router.message(F.text == 'Вторник_11А')
async def tuesday_11a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_11а'])


@router.message(F.text == 'Среда_11А')
async def wednesday_11a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_11а'])


@router.message(F.text == 'Четверг_11А')
async def thursday_11a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_11а'])


@router.message(F.text == 'Пятница_11А')
async def friday_11a_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_11а'])


@router.message(F.text == 'Понедельник_11Б')
async def monday_11b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_11б'])


@router.message(F.text == 'Вторник_11Б')
async def tuesday_11b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_11б'])


@router.message(F.text == 'Среда_11Б')
async def wednesday_11b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_11б'])


@router.message(F.text == 'Четверг_11Б')
async def thursday_11b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_11б'])


@router.message(F.text == 'Пятница_11Б')
async def friday_11b_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_11б'])


@router.message(F.text == 'Понедельник_11В')
async def monday_11v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['понедельник_11в'])


@router.message(F.text == 'Вторник_11В')
async def tuesday_11v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['вторник_11в'])


@router.message(F.text == 'Среда_11В')
async def wednesday_11v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['среда_11в'])


@router.message(F.text == 'Четверг_11В')
async def thursday_11v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['четверг_11в'])


@router.message(F.text == 'Пятница_11В')
async def friday_11v_day_command(m: Message):
    await m.answer(text=LEXICON_RU['пятница_11в'])
