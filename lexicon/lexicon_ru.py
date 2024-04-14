import openpyxl as xl

book = xl.open('lessons_schedule.xlsx')

sheet = book.active

LEXICON_RU: dict[str, str] = {
    'start': '<b>Привет!</b>',
    'контакты': 'Директор:\n'
                'Шишмек Ольга Владимировна\n'
                '+7 (495) 625-24-53\n'
                'ShimshekOV@edu.mos.ru\n\n'
                'Секретарь учебной части:\n'
                'Сильянова Светлана Алексеевна\n'
                '+7 (495) 625-24-53\n'
                '1284@edu.mos.ru\n\n'
                'Зам директора по воспитанию и социализации обучающихся:\n'
                'Журавлёва Анна Сергеевна\n'
                '+7 (495) 625-24-53\n'
                'zhuravlevaas@sch1284.mskobr.ru\n\n'
                'Зам директора по содержанию образования и конвергенции образовательных программ:\n'
                'Мавлеева Наталья Васильевна\n'
                '+7 (495) 621-93-72\n'
                'mavleevanv@sch1284.mskobr.ru\n\n'
                'Зам директора по контролю качества образования:\n'
                'Соломатова Анна Михайловна\n'
                '+7 (495) 625-24-53\n'
                'solomatovaam@sch1284.mskobr.ru\n\n'
                'Первый зам директора по управлению ресурсами:\n'
                'Мороз Александр Анатольнвич\n'
                '+7 (495) 625-24-53\n'
                'MorozAA@sch1284.mskobr.ru\n\n'
                'По вопросам питания:\n'
                'Балалаева Наталья Анатольевна\n'
                '+7 (495) 623-61-57\n'
                'balalaevana@sch1284.mskobr.ru',
    'группы_школы': '🏫Телеграм канал школы №1284:\n'
                    'https://t.me/school_1284\n\n'
                    '💎Телеграм канал Ученического самоуправления нашей школы:\n'
                    'https://t.me/samoupravlenie1284\n\n'
                    '✍🏻Телеграм канал Подслушано 1284:\n'
                    'https://t.me/schoolnews1284\n\n'
                    '🏀Телеграм канал Школьного спортивного клуба Heartbeat:\n'
                    'https://t.me/sportclub_school1284',
    'расписание_звонков': 'лялялля',
    'расписание_уроков': 'ляляляляля',
    'понедельник11а': 'пук-пук',

}