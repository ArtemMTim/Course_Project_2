import requests
from abc import ABC, abstractmethod
import json
import os
from config import DATA_DIR


class Parser(ABC):
    """Абстрактный класс по работе с API сервисами.
    Загружает, обрабатывает, возвращает и записывает в файл данные."""

    @abstractmethod
    def load_vacancies(self):
        pass

    @abstractmethod
    def export_vac_list(self):
        pass

    @abstractmethod
    def write_file(self):
        pass


class HH(Parser):
    """Класс для работы с API сервиса HeadHunter.
    Получает список вакансий по ключевому слову.
    Полученный список приводит к необходимому виду, описанному в README.
    Класс является дочерним классом класса Parser."""

    def __init__(self, filename):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        self.vacancies_short = []
        self.fullname = os.path.join(DATA_DIR, filename)

    def load_vacancies(self, keyword):
        """Метод загружает вакансии с сервиса HH. Формирует из загруженных данных список вакансий
        с полями: название, ссылка, зарплата, описание, требования, место."""
        self.params["text"] = keyword
        while self.params.get("page") != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
            for vacancie in self.vacancies:
                if vacancie["name"]:
                    title = vacancie["name"]
                else:
                    title = "Не указано."
                if vacancie["alternate_url"]:
                    link = vacancie["alternate_url"]
                else:
                    link = "Не указано."
                if vacancie["snippet"]["responsibility"]:
                    description = vacancie["snippet"]["responsibility"]
                else:
                    description = "Не указано."
                if vacancie["snippet"]["requirement"]:
                    requirement = vacancie["snippet"]["requirement"]
                else:
                    requirement = "Не указано."
                if vacancie["salary"]:
                    if vacancie["salary"]["from"]:
                        salary = vacancie["salary"]["from"]
                else:
                    salary = 0
                if vacancie["area"]["name"]:
                    area = vacancie["area"]["name"]
                else:
                    area = "Не указано."
                self.vacancies_short.append(
                    {
                        "title": title,
                        "link": link,
                        "description": description,
                        "requirement": requirement,
                        "salary": salary,
                        "area": area,
                    }
                )

    def export_vac_list(self):
        """Метод возвращает обработанный список вакансий."""
        return self.vacancies_short

    def write_file(self):
        """Метод записывает обработанный список вакансий в указанный файл."""
        with open(self.fullname, "w", encoding="utf-8") as file:
            json.dump(self.vacancies_short, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    hh = HH("test.json")
    hh.load_vacancies("Зоолог")
    hh.write_file()
