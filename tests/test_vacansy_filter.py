from src.vacansy import Vacansy
from src.vacansy_filter import VacansyFilter
import pytest


def test_vacansy_filter_set_get_list(vacansy_list_for_filter):
    """Тестирование получения и возвращения списка вакансий."""
    test = VacansyFilter()
    test.vacs = vacansy_list_for_filter
    assert test.vacs == vacansy_list_for_filter


def test_vacansy_filter_title(vacansy_list_for_filter):
    """Тестирование фильтрации вакансий по названию вакансии."""
    test = VacansyFilter()
    test.vacs = vacansy_list_for_filter
    test.filter_title("Продавец")
    assert test.vacs == [vacansy_list_for_filter[1]]


def test_vacansy_filter_description(vacansy_list_for_filter):
    """Тестирование фильтрации вакансий по описанию."""
    test = VacansyFilter()
    test.vacs = vacansy_list_for_filter
    test.filter_descriprtion("Технич")
    assert test.vacs == [vacansy_list_for_filter[0]]


def test_vacansy_filter_requirement(vacansy_list_for_filter):
    """Тестирование фильтрации вакансий по требованию."""
    test = VacansyFilter()
    test.vacs = vacansy_list_for_filter
    test.filter_requirement("высш")
    assert test.vacs == [vacansy_list_for_filter[0]]


def test_vacansy_filter_salary(vacansy_list_for_filter):
    """Тестирование фильтрации вакансий по зарплате."""
    test = VacansyFilter()
    test.vacs = vacansy_list_for_filter
    test.filter_salary(50000)
    assert test.vacs == vacansy_list_for_filter


def test_vacansy_filter_area(vacansy_list_for_filter):
    """Тестирование фильтрации вакансий по местоположению."""
    test = VacansyFilter()
    test.vacs = vacansy_list_for_filter
    test.filter_area("химки")
    assert test.vacs == [vacansy_list_for_filter[1]]
