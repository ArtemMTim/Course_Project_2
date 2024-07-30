import json
import os

from config import DATA_DIR
from src.vacansy import Vacansy


class VacansyList:
    """Класс, принимает название json файла с вакансиями (название также задано по-умолчанию).
    Читает указанный файл в папке data проекта,
    выводит список вакансий как в str виде так и в расширенном виде.
    Позволяет создавать и редактировать список вакансий - добавлять вакансии, удалять их по индексу.
    Изменённый список позволяет записать в заданный файл."""

    filename: str

    def __init__(self, filename="vacansies.json"):
        self.filename = filename
        self.fullname = os.path.join(DATA_DIR, filename)
        self.vacs_list = []

    def read_file(self) -> None:
        """Метод читает указанный файл и сохраняет список объектов вакансий из файла."""
        with open(self.fullname, "r", encoding="UTF-8") as file:
            temp_info = json.load(file)
        self.vacs_list = [Vacansy(**item) for item in temp_info]

    def show_vacansy_list(self):
        """Метод выводит расширенную информацию о вакансиях из списка объектов вакансий с номерами."""
        if len(self.vacs_list) == 0:
            return []
        num = 0
        result_info = ""
        for item in self.vacs_list:
            num += 1
            result_info += f"Номер - {num} Вакансия: {item.title}, зарплата: {item.salary}, местоположение: {item.area}, описание: {item.description}, требования: {item.requirement}, ссылка: {item.link}\n"
        return result_info

    def show_str_vacs(self):
        """Метод выводит сокращённую информацию о вакансиях из списка объектов вакансий с номерами."""
        if len(self.vacs_list) == 0:
            return []
        num = 0
        result_info = ""
        for item in self.vacs_list:
            num += 1
            result_info += f"Номер - {num} {str(item)}\n"
        return result_info

    def show_vacansy_by_index(self, index):
        """Метод выводит расширенную информацию о вакансии по заданному индексу."""
        item = self.vacs_list[index - 1]
        return f"Вакансия: {item.title}, зарплата: {item.salary}, местоположение: {item.area}, описание: {item.description}, требования: {item.requirement}, ссылка: {item.link}"

    def add_vacansy(self, vacansy: dict) -> None:
        """Метод добавляет объект вакансии в список вакансий,
        принимая данные в виде словаря с описанием вакансии, объекта вакнсии, списка словарей,
        либо списка объектов вакансий."""
        if isinstance(vacansy, dict):
            new_vacansy = Vacansy(**vacansy)
            self.vacs_list.append(new_vacansy)
        elif isinstance(vacansy, Vacansy):
            self.vacs_list.append(vacansy)
        elif isinstance(vacansy, list) or isinstance(vacansy, tuple):
            for item in vacansy:
                if isinstance(item, dict):
                    new_vacansy = Vacansy(**item)
                    self.vacs_list.append(new_vacansy)
                elif isinstance(item, Vacansy):
                    self.vacs_list.append(item)

    def del_vacansy(self, number: int) -> None:
        """Метод удаляет из списка объект вакансии по номеру (индексу)."""
        self.vacs_list.pop(number - 1)

    def write_new_vac_list(self) -> None:
        """Метод записывает обработанный список вакансий в исходный файл, тем самым изменяя список в нём."""
        try:
            temp_vac_list = []
            for item in self.vacs_list:
                temp_vac_list.append(
                    {
                        "title": item.title,
                        "salary": item.salary,
                        "area": item.area,
                        "description": item.description,
                        "requirement": item.requirement,
                        "link": item.link,
                    }
                )
            with open(self.fullname, "w", encoding="utf-8") as file:
                json.dump(temp_vac_list, file, ensure_ascii=False, indent=4)
            print("Файл записан")
        except:
            raise ValueError("При записи файла произошла ошибка!")

    def export_vacansy_list(self):
        """Метод возвращает список объектов вакансий."""
        return self.vacs_list

    def import_vacansy_list(self, new_list):
        """Метод принимает новый список объектов вакансий и заменяет им старый."""
        self.vacs_list = new_list


if __name__ == "__main__":
    file = VacansyList("vacs.json")
    print(file.filename)
    # Чтение файла
    file.read_file()
    # Вывод считанного списка
    # print(file.show_vacansy_list())
    # Удаление вакансии по индексу
    # file.del_vacansy(0)
    # Вывод изменённого списка
    # print(file.show_vacansy_list())

    vac1 = {
        "title": "Инженер 1 кат",
        "salary": 150000,
        "link": "artemtim.ru",
        "area": "Москва",
        "description": "Работа с технической документацией",
        "requirement": "Опрыт работы от 5 лет. Высшее образование.",
    }
    vac2 = {
        "title": "Инженер 2 кат",
        "salary": 70000,
        "link": "artemtim.ru",
        "area": "Москва",
        "description": "Работа с технической документацией",
        "requirement": "Опрыт работы от 2 лет. Высшее образование.",
    }
    # Добавление вакансии в виде словаря
    # file.add_vacansy(vac1)
    # print(file.show_vacansy_list())
    # Добавление вакансии в виде объекта Vacansy
    # file.add_vacansy(Vacansy(**vac2))
    # print(file.show_vacansy_list())
    # Добавление вакансий в виде списка словарей
    # file.add_vacansy([vac1, vac2])
    # print(file.show_vacansy_list())
    # Добавление вакансий в виде списка объектов Vacansy
    # file.add_vacansy([Vacansy(**vac1), Vacansy(**vac2)])
    # print(file.show_vacansy_list())
    # Запись отредактированного списка в файл
    # file.write_new_vac_list()
    # Чтение файла
    # file.read_file()
    # Вывод считанного списка
    print(file.show_str_vacs())
    # Вывод информации о вакансии по индексу
    print(file.show_vacansy_by_index(6))
