from src.classes import Vacansy
import pytest

def test_vacansy_init(vacansy_1):
    assert vacansy_1.title == 'Инженер'
    assert vacansy_1.link == 'artemtim.ru'
    assert vacansy_1.salary == 50000
    assert vacansy_1.description == 'Работа с технической документацией'
    assert vacansy_1.requirement == 'Опрыт работы от 3 лет. Высшее образование.'