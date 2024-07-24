import pytest

from src.file import WorkWithFile


# Тест инициализации класса WorkWithFile
def test_work_with_file_init(file_name):
    assert WorkWithFile(file_name).filename == "test_file_name.json"


def test_work_with_file_adding_vac(vacansy_1):
    file = WorkWithFile()
    file.add_vacansy_object(vacansy_1)
    assert (
        file.show_vacansy_by_index(0)
        == "Вакансия: Инженер, зарплата: 50000, ссылка: artemtim.ru, описание: Работа с технической документацией, требования: Опрыт работы от 3 лет. Высшее образование."
    )


def test_work_with_file_adding_list_obj(vacansy_list):
    file = WorkWithFile()
    file.add_vacansy_list(vacansy_list)
    assert file.show_str_vacs() == (
        "Номер - 1 Вакансия - Инженер 1кат, зарплата - 90000, ссылка на вакансию - artemtim.ru.\n"
        "Номер - 2 Вакансия - Инженер, зарплата - 50000, ссылка на вакансию - artemtim.ru.\n"
    )
