from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


@router.message(F.text == '👨🏻Общее👩🏻')
async def standart_break_schedule(m: Message):
    await m.answer(text=LEXICON_RU['общее_расписание_звонков'])


@router.message(F.text == '👶Начальная школа')
async def primary_break_schedule(m: Message):
    await m.answer(text=LEXICON_RU['расписание_начальных_классов'])
