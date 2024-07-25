import pytest

from src.vacansy import Vacansy


@pytest.fixture
def vacansy_list():
    return [
        Vacansy(
            title="Инженер 1кат",
            link="artemtim.ru",
            salary=90000,
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


@pytest.fixture
def vacansy_list_for_filter():
    return [
        Vacansy(
            title="Инженер 1кат",
            link="artemtim.ru",
            salary=90000,
            description="Работа с технической документацией",
            requirement="Опрыт работы от 3 лет. Высшее образование.",
        ),
        Vacansy(
            title="Продавец",
            link="artemtim.ru",
            salary=50000,
            description="Продажа томатов",
            requirement="Опрыт работы от 2 лет.",
        ),
    ]


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
