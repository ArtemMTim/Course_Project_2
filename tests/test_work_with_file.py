import pytest

from src.classes import WorkWithFile


# Тест инициализации класса WorkWithFile
def test_work_with_file_init(file_name):
    assert WorkWithFile(file_name).filename == "test_file_name.json"
