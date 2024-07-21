import pytest

from src.classes import Vacansy
from src.utils import info_vacansy_from_object


def test_info_vacansy(vacansy_1):
    assert (
        info_vacansy_from_object(vacansy_1)
        == f"""Вакансия: {vacansy_1.title}, зарплата: {vacansy_1.salary}, 
    ссылка: {vacansy_1.link}, описание: {vacansy_1.description},
     требования: {vacansy_1.requirement}"""
    )
