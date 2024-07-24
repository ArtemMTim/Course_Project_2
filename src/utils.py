import json
import os

from config import DATA_DIR
from src.vacansy import Vacansy


def info_vacansy_from_object(vac_object: Vacansy) -> str:
    return f"""Вакансия: {vac_object.title}, зарплата: {vac_object.salary}, 
    ссылка: {vac_object.link}, описание: {vac_object.description},
     требования: {vac_object.requirement}"""


def get_vac_object_from_file(file_name="vacs.json"):
    full_filename = os.path.join(DATA_DIR, file_name)
    with open(full_filename, "r", encoding="UTF-8") as file:
        temp_info = json.load(file)
    vacs_list = [Vacansy(**item) for item in temp_info]
    return vacs_list


def get_file_from_vacs(vac_object_list, file_name="vacs.json"):
    temp_vac_list = []
    for item in vac_object_list:
        temp_vac_list.append(
            {
                "title": item.title,
                "salary": item.salary,
                "link": item.link,
                "description": item.description,
                "requirement": item.requirement,
            }
        )
    full_filename = os.path.join(DATA_DIR, file_name)
    with open(full_filename, "w", encoding="utf-8") as file:
        json.dump(temp_vac_list, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    get_file_from_vacs(
        [
            Vacansy(
                title="Инженер",
                link="artemtim.ru",
                salary=50000,
                description="Работа с технической документацией",
                requirement="Опрыт работы от 3 лет. Высшее образование.",
            ),
            Vacansy(
                title="Инженер",
                link="artemtim.ru",
                salary=50000,
                description="Работа с технической документацией",
                requirement="Опрыт работы от 3 лет. Высшее образование.",
            ),
        ]
    )
    print(get_vac_object_from_file())
