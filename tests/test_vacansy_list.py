import pytest

from src.vacansy_list import VacansyList


def test_vacansy_list_init(file_name):
    """Тестирование инициализации."""
    assert VacansyList(file_name).filename == "test_file_name.json"


def test_vacansy_list_adding_vac(vacansy_1):
    """Тестирование добавления объекта вакансий в список."""
    file = VacansyList()
    file.add_vacansy(vacansy_1)
    assert (
        file.show_vacansy_by_index(0)
        == "Вакансия: Инженер, зарплата: 50000, ссылка: artemtim.ru, описание: Работа с технической документацией, требования: Опрыт работы от 3 лет. Высшее образование."
    )


def test_vacansy_list_adding_list_obj(vacansy_list):
    """Тестирование добавления списка объектов вакансий в список."""
    file = VacansyList()
    file.add_vacansy(vacansy_list)
    assert file.show_str_vacs() == (
        "Номер - 1 Вакансия - Инженер 1кат, зарплата - 90000, ссылка на вакансию - artemtim.ru.\n"
        "Номер - 2 Вакансия - Инженер, зарплата - 50000, ссылка на вакансию - artemtim.ru.\n"
    )


def test_vacansy_list_export_import(vacansy_list):
    """Тестирование импорта и экспорта списка вакансий."""
    test = VacansyList()
    test.import_vacansy_list(vacansy_list)
    assert test.export_vacansy_list() == vacansy_list
    assert test.show_str_vacs() == (
        "Номер - 1 Вакансия - Инженер 1кат, зарплата - 90000, ссылка на вакансию - artemtim.ru.\n"
        "Номер - 2 Вакансия - Инженер, зарплата - 50000, ссылка на вакансию - artemtim.ru.\n"
    )
