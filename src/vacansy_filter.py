from src.vacansy import Vacansy
import re


class VacansyFilter:
    """Класс фильтрует список объектов вакансий по заданным признакам. Возвращает отфильтрованный список."""

    def __init__(self):
        self.__vacs = []

    @property
    def vacs(self):
        return self.__vacs

    @vacs.setter
    def vacs(self, vacs):
        if isinstance(vacs, list):
            self.__vacs = vacs
        else:
            raise ValueError("Некорректные данные")

    def filter_salary(self, salary):
        """Метод проводит фильтрование списка объектов вакансий по зарплате(более заданного значения)."""
        self.__vacs = [item for item in self.__vacs if item.salary >= salary]

    def filter_title(self, word):
        """Метод проводит фильтрование списка объектов вакансий по названию вакансии (совпадению заданного слова)."""
        pattern = rf"{word}"
        self.__vacs = [item for item in self.__vacs if re.findall(pattern, item.title, re.IGNORECASE)]

    def filter_descriprtion(self, word):
        """Метод проводит фильтрование списка объектов вакансий по описанию вакансии (совпадению заданного слова)."""
        pattern = rf"{word}"
        self.__vacs = [item for item in self.__vacs if re.findall(pattern, item.description, re.IGNORECASE)]

    def filter_requirement(self, word):
        """Метод проводит фильтрование списка объектов вакансий по требованию к вакансии (совпадению заданного слова)."""
        pattern = rf"{word}"
        self.__vacs = [item for item in self.__vacs if re.findall(pattern, item.requirement, re.IGNORECASE)]


if __name__ == "__main__":
    new_vacs = [
        Vacansy(
            title="Инженер 1кат",
            link="artemtim.ru",
            salary=90000,
            description="Работа с технической документацией",
            requirement="Опрыт работы от 5 лет. Высшее образование.",
        ),
        Vacansy(
            title="Инженер",
            link="artemtim.ru",
            salary=50000,
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
    test.filter_requirement("5 Лет")
    print(test.vacs)
