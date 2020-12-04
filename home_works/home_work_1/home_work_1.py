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

from urllib import parse
from http.cookies import SimpleCookie


def parse_parameters(url):
    """
    Функция "parse_parameters" принимает строку запроса и извлекает (парсить) из нее переданные
    параметры, результат возвращает в виде словаря.
    """
    res = dict(parse.parse_qsl(parse.urlsplit(url).query))
    return res


def parse_cookies(raw_data):
    """
    Функция "parse_cookies" принимает строку куков и извлекает (парсит) из нее куки, результат
    возвращает в виде словаря.
    """
    cookie = SimpleCookie()
    cookie.load(raw_data)
    dict_cookies = {}
    for key, data_cookie in cookie.items():
        dict_cookies[key] = data_cookie.value
    return dict_cookies


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('http://example.com/') == {}
    assert parse_parameters('https://test_2.com/par=app') == {'par': 'app'}
    assert parse_parameters('https://example.com/path/to/page?\
                            name=ferret&color=purple') == {'name': 'ferret',
                                                           'color': 'purple'}
    assert parse_parameters('https://example.com/page?name=Alex\
                            &age=21') == {'name': 'Alex',
                                          'age': '21'}
    assert parse_parameters('http://example.com/page/?name=Alexandr\
                            &age=22') == {'name': 'Alexandr',
                                          'age': '22'}
    assert parse_parameters('https://test_1.com/page?fruit=apple&color=red\
                            &price=14.00') == {'fruit': 'apple',
                                               'color': 'red',
                                               'price': '14.00'}
    assert parse_parameters('http://e-catalog.ua/page?name=HP\
                            &model=Pavillion_dv5') == {'name': 'HP',
                                                       'model': 'Pavillion_dv5'}
    assert parse_parameters('https://exam.com/page?name=Tests\
                            &page=21') == {'name': 'Tests',
                                           'page': '21'}
    assert parse_parameters('http://googlemap.com/page/?country=Ukraine\
                            &city=Odessa') == {'country': 'Ukraine',
                                               'city': 'Odessa'}
    assert parse_parameters('https://test_2.com/page?par=app') == {'par': 'app'}
    assert parse_parameters('http://e-catalog.ua/page?category=PC&model=DELL\
                            &color=black') == {'category': 'PC',
                                               'model': 'DELL',
                                               'color': 'black'}

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('devicePixelRatio=1;\
                        ident=exists;\
                        __utma=13103r6942.2918;\
                        __utmc=13103656942;') == {'devicePixelRatio': '1',
                                                  'ident': 'exists',
                                                  '__utma': '13103r6942.2918',
                                                  '__utmc': '13103656942'}
    assert parse_cookies('name=ferret;color=purple;') == {'name': 'ferret', 'color': 'purple'}
    assert parse_cookies('name=Alex;age=21;') == {'name': 'Alex', 'age': '21'}
    assert parse_cookies('fruit=apple;color=red;price=14.00;') == {'fruit': 'apple',
                                                                   'color': 'red',
                                                                   'price': '14.00'}
    assert parse_cookies('name=HP;model=Pavillion_dv5;') == {'name': 'HP',
                                                             'model': 'Pavillion_dv5'}
    assert parse_cookies('name=Tests;page=21;par=app;') == {'name': 'Tests',
                                                            'page': '21',
                                                            'par': 'app'}
    assert parse_cookies('country=Ukraine;city=Odessa;') == {'country': 'Ukraine', 'city': 'Odessa'}
    assert parse_cookies('category=PC;model=DELL;color=black;') == {'category': 'PC',
                                                                    'model': 'DELL',
                                                                    'color': 'black'}
