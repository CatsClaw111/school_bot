import openpyxl as xl

book = xl.open('lessons_schedule.xlsx')

sheet = book.active

LEXICON_RU: dict[str, str] = {
    'start': '<b>Привет!</b>',
    'расписание_звонков': 'лялялля',
    'понедельник11а': 'пук-пук',

}