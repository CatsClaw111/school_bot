from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


@router.message(F.text == '🗂Соц-эк')
async def soc_ek_tea_command(m: Message):
    await m.answer(text=LEXICON_RU['соц_эк_учителя'])


@router.message(F.text == '🗣Гум')
async def gum_tea_command(m: Message):
    await m.answer(text=LEXICON_RU['гум_учителя'])


@router.message(F.text == '🗣Гум ин.яз.')
async def gum_tea_command(m: Message):
    await m.answer(text=LEXICON_RU['гум_учителя_ин_яз'])


@router.message(F.text == '💻Тех')
async def tech_tea_command(m: Message):
    await m.answer(text=LEXICON_RU['тех_учителя'])


@router.message(F.text == '🧪Ест-науч')
async def biohim_tea_command(m: Message):
    await m.answer(text=LEXICON_RU['ест_науч_учителя'])


@router.message(F.text == '📚Иные учителя')
async def other_tea_command(m: Message):
    await m.answer(text=LEXICON_RU['иные_учителя'])


@router.message(F.text == '🖊Иной пед. персонал')
async def other_pre_command(m: Message):
    await m.answer(text=LEXICON_RU['иной_пед_персонал'])


@router.message(F.text == '🧸Начальные классы')
async def pri_tea_command(m: Message):
    await m.answer(text=LEXICON_RU['учителя_начальных_классов'])
