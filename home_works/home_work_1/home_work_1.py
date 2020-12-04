"""
Вам дан шаблон main.py, в шаблоне объявлены две функции "parse_parameters" и "parse_cookies"
(шаблоны). Необходимо реализовать функционал данных функций и написать по 10 тестов к каждой из
функций, в шаблоне, в качестве примера, уже написано по два теста на каждую функцию.

Функция "parse_parameters" должна принимать строку запроса и извлекать (парсить) из нее переданные
параметры, результат возвращать в виде словаря

Функция "parse_cookies" должна принимать строку куков и извлекать (парсить) из нее куки, результат
возвращать в виде словаря

Рекомендуемый порядок работы:
    - Создать рабочую папку
    - Инициализировать пустой репозиторий Git командой git init
    - Создать пустой репозиторий в своем аккаунте на GitHub
    - Добавить сокращенное имя "origin" и добавить информацию о удаленном репозитории командой
    - git remote add origin YOUR_URL
    - Скопировать предоставленный шаблон main.py в рабочую папку
    - Выполнить первый комит с шаблоном main.py
    - Реализовать необходимую функциональность, каждый осмысленный этап работы оформлять комитом в
    Git-репозиторий (использовать одну ветку или несколько, а также как именно распределить
    комиты - это на ваше усмотрение)
    - Залить все комиты на удаленный репозиторий (фактически в ваш GitHub-аккаунт)
В качестве ответа предоставить ссылку на GitHub-репозиторий
"""


def parse_parameters(url):
    from urllib import parse
    res = dict(parse.parse_qsl(parse.urlsplit(url).query))
    return res