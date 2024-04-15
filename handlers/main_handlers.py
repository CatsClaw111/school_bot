from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.start_keyboard import start_key
from keyboards.break_schedule_keyboards import break_key
from keyboards.lessons_keyboards.parallel_keyboards import par_key
from keyboards.teacher_keyboards import tea_key
router = Router()


@router.message(F.text == '/start')
async def start_command(m: Message):
    await m.answer(text=LEXICON_RU['start'],
                   reply_markup=start_key)


@router.message(F.text == '🗓Расписание уроков')
async def lessons_schedule_command(m: Message):
    await m.answer(text=LEXICON_RU['расписание_уроков'],
                   reply_markup=par_key)


@router.message(F.text == '🛎️Расписание звонков')
async def break_schedule_command(m: Message):
    await m.answer(text=LEXICON_RU['расписание_звонков'],
                   reply_markup=break_key)


@router.message(F.text == '👨‍🏫Учителя👩‍🏫')
async def teachers_command(m: Message):
    await m.answer(text=LEXICON_RU['учителя'],
                   reply_markup=tea_key)


@router.message(F.text == '🗄Контакты')
async def contacts_command(m: Message):
    await m.answer(text=LEXICON_RU['контакты'])


@router.message(F.text == '🌐Группы школы')
async def groups_command(m: Message):
    await m.answer(text=LEXICON_RU['группы_школы'])

@router.message(F.text == '📋В главное меню')
async def return_menu_command(m: Message):
    await m.answer(text=LEXICON_RU['start'],
                   reply_markup=start_key)