from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.start_keyboard import start_key

router = Router()

@router.message(F.text == 'Понедельник_11А')
async def monday_11a(m: Message):
    await m.answer(text=LEXICON_RU['понедельник11а'])