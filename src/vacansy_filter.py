from src.vacansy import Vacansy
import re


class VacansyFilter:
    """Класс фильтрует список объектов вакансий по заданным признакам, сортирует по зарплате (по-умолчанию по возростанию).
    Возвращает отфильтрованный и отсортированный список."""

    def __init__(self):
        self.__vacs = []

    @property
    def vacs(self):
        return self.__vacs

    @vacs.setter
    def vacs(self, vacs):
        if isinstance(vacs, list):
            self.__vacs = []
            self.__vacs = vacs
        else:
            raise ValueError("Некорректные данные")

    def filter_salary(self, salary):
        """Метод проводит фильтрование списка объектов вакансий по зарплате(более заданного значения)."""
        temp = filter(lambda x: x.salary >= salary, self.__vacs)
        self.__vacs = list(temp)

    def filter_title(self, word):
        """Метод проводит фильтрование списка объектов вакансий по названию вакансии (совпадению заданного слова)."""
        pattern = rf"{word}"
        temp = filter(lambda x: re.findall(pattern, x.title, re.IGNORECASE), self.__vacs)
        self.__vacs = list(temp)

    def filter_descriprtion(self, word):
        """Метод проводит фильтрование списка объектов вакансий по описанию вакансии (совпадению заданного слова)."""
        pattern = rf"{word}"
        temp = filter(lambda x: re.findall(pattern, x.description, re.IGNORECASE), self.__vacs)
        self.__vacs = list(temp)

    def filter_requirement(self, word):
        """Метод проводит фильтрование списка объектов вакансий по требованию к вакансии (совпадению заданного слова)."""
        pattern = rf"{word}"
        temp = filter(lambda x: re.findall(pattern, x.requirement, re.IGNORECASE), self.__vacs)
        self.__vacs = list(temp)

    def filter_area(self, word):
        """Метод проводит фильтрование списка объектов вакансий по местоположению (совпадению заданного слова)."""
        pattern = rf"{word}"
        temp = filter(lambda x: re.findall(pattern, x.area, re.IGNORECASE), self.__vacs)
        self.__vacs = list(temp)

    def sort_by_salary(self, direction=False):
        """Метод сортирует список объектов вакансий по зарплате (по-умолчанию по возрастанию)"""
        self.__vacs.sort(key=lambda x: x.salary, reverse=direction)


if __name__ == "__main__":
    new_vacs = [
        Vacansy(
            title="Инженер 1кат",
            link="artemtim.ru",
            area="Москва",
            salary=90000,
            description="Работа с технической документацией",
            requirement="Опрыт работы от 5 лет. Высшее образование.",
        ),
        Vacansy(
            title="Инженер",
            link="artemtim.ru",
            salary=50000,
            area="Москва",
            description="Работа на заводе",
            requirement="Опрыт работы от 2 лет. Высшее образование.",
        ),
    ]
    test = VacansyFilter()
    test.vacs = new_vacs
    print(test.vacs)
    # test.filter_salary(70000)
    # test.filter_title('1кат')
    # test.filter_descriprtion('завод')
    # test.filter_requirement("5 Лет")
    # test.filter_area("москва")
    test.sort_by_salary()
    print(test.vacs)
