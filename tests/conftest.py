import pytest

from src.classes import Vacansy


@pytest.fixture
def vacansy_1():
    return Vacansy(
        title="Инженер",
        link="artemtim.ru",
        salary=50000,
        description="Работа с технической документацией",
        requirement="Опрыт работы от 3 лет. Высшее образование.",
    )

@pytest.fixture
def vacansy_2():
    return Vacansy(
        title="Инженер 1кат",
        link="artemtim.ru",
        salary=90000,
        description="Работа с технической документацией",
        requirement="Опрыт работы от 3 лет. Высшее образование.",
    )


@pytest.fixture
def file_name():
    return "test_file_name.json"
