import json
import os
from functools import total_ordering

import requests

from config import DATA_DIR


@total_ordering
class Vacansy:
    """Класс, описывающий вакансию и её основные характеристики"""

    title: str
    link: str
    salary: int | float
    description: str
    requirement: str

    def __init__(self, title, link, description, requirement, salary=0):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description
        self.requirement = requirement

    def __str__(self):
        return f"Вакансия - {self.title}, зарплата - {self.salary}, ссылка на вакансию - {self.link}."

    def __eq__(self, other):
        if isinstance(other, Vacansy):
            return self.salary == other.salary
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Vacansy):
            return self.salary < other.salary
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Vacansy):
            return self.salary >= other.salary
        else:
            return NotImplemented


class WorkWithFile:
    """Класс, принимает название json файла с вакансиями. Читает указанный файл в папке data проекта,
    выводит в консоль список вакансий. Позволяет добавлять вакансии, удалять их по номеру вывода.
    Изменённый список записывает в исходный файл."""

    filename: str

    def __init__(self, filename):
        self.filename = filename
        self.fullname = os.path.join(DATA_DIR, filename)

    def read_file(self) -> None:
        with open(self.fullname, "r", encoding="UTF-8") as file:
            temp_info = json.load(file)
        self.vacs_list = [Vacansy(**item) for item in temp_info]
        num = 0
        for item in self.vacs_list:
            num += 1
            print(
                f"Номер - {num} Вакансия: {item.title}, зарплата: {item.salary}, ссылка: {item.link}, описание: {item.description}, требования: {item.requirement}"
            )

    def add_vacansy(self, vacansy: dict) -> None:
        new_vacansy = Vacansy(**vacansy)
        self.vacs_list.append(new_vacansy)
        num = 0
        for item in self.vacs_list:
            num += 1
            print(
                f"Номер - {num} Вакансия: {item.title}, зарплата: {item.salary}, ссылка: {item.link}, описание: {item.description}, требования: {item.requirement}"
            )

    def del_vacansy(self, number: int) -> None:
        self.vacs_list.pop(number - 1)
        num = 0
        for item in self.vacs_list:
            num += 1
            print(
                f"Номер - {num} Вакансия: {item.title}, зарплата: {item.salary}, ссылка: {item.link}, описание: {item.description}, требования: {item.requirement}"
            )

    def write_new_vac_list(self) -> None:
        temp_vac_list = []
        for item in self.vacs_list:
            temp_vac_list.append(
                {
                    "title": item.title,
                    "salary": item.salary,
                    "link": item.link,
                    "description": item.description,
                    "requirement": item.requirement,
                }
            )
        with open(self.fullname, "w", encoding="utf-8") as file:
            json.dump(temp_vac_list, file, ensure_ascii=False, indent=4)
        print("Файл записан")


if __name__ == "__main__":
    file = WorkWithFile("vacs.json")
    print(file.filename)
    file.read_file()
    # file.del_vacansy(6)
    vac1 = {
        "title": "Инженер 1 кат",
        "salary": 150000,
        "link": "artemtim.ru",
        "description": "Работа с технической документацией",
        "requirement": "Опрыт работы от 5 лет. Высшее образование.",
    }
    vac2 = {
        "title": "Инженер 2 кат",
        "salary": 70000,
        "link": "artemtim.ru",
        "description": "Работа с технической документацией",
        "requirement": "Опрыт работы от 2 лет. Высшее образование.",
    }
    file.add_vacansy(vac1)
    file.add_vacansy(vac2)
    file.write_new_vac_list()
