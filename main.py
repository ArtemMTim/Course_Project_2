from src.vacansy import Vacansy
from src.vacansy_api import HH
from src.vacansy_filter import VacansyFilter
from src.vacansy_list import VacansyList
from src.vacansy_file import VacansyFile


def main_func():
    # Приветствие и краткое описание возможностей программы.
    print("Вас приветствует программа по работе с вакансиями!")
    print(
        """Данная программа позволяет:
    - получать вакансии от сервиса HH по ключевому слову;
    - получать список вакансий, отфильтрованный по определённому параметру*;
    - получать список вакансий отсортированный по зарплате;
    - записать полученный в ходе обработки список в файл.
    
    * Параметры, доступные для применения в операции фильтрования вакансий:
    - зарплата (не ниже указанного значения);
    - описание вакансии по определённым словам;
    - требования к вакансии по определённым словам;
    - местоположение вакансии по определённому слову (название города)."""
    )

    # Запрос ключевого слова для поиска.
    print("По какому слову будем искать вакансии?")
    key_word_for_vacs = input("Введите слово для поиска вакансий здесь: ")
    # Получение вакансий по ключевому слову с сервиса HH.
    hh_vacs = HH()
    hh_vacs.load_vacancies(key_word_for_vacs)
    # Экспортируем список вакансий для дальнейщей обработки.
    temp_vacs_list = hh_vacs.export_vac_list()

    # Запрос слов для фильтрации вакансий
    print("По каким параметрам будем фильтровать вакансии?")
    req_word = input("Введите слово, по которому будем фильтровать вакансии в требованиях к вакансии или нажмите ввод: ")
    descr_word = input("Введите слово, по которому будем фильтровать вакансии в описании вакансии или нажмите ввод: ")
    area_word = input("Введите название города, по которому будем фильтровать вакансии или нажмите ввод: ")
    salary_num = int(input("Введите значение зарплаты, ниже которого вакансии будут отфильтрованы: "))

    # Обрабатываем список вакансий согласно запрошенных слов.

    v_filter = VacansyFilter()
    v_filter.vacs = temp_vacs_list
    v_filter.filter_requirement(req_word)
    print('Вакансии отфильтрованы по требованиям.')
    v_filter.filter_descriprtion(descr_word)
    print('Вакансии отфильтрованы по описанию.')
    v_filter.filter_area(area_word)
    print('Вакансии отфильтрованы по местоположению.')
    v_filter.filter_salary(salary_num)
    print('Вакансии отфильтрованы по зарплате.')

    # Сортируем вакансии по уменьшению зарплаты
    v_filter.sort_by_salary(True)

    temp_vacs_list = v_filter.vacs

    # Передаём обработанный список для отображения топа вакансий и записи в файл.

    vacs_list = VacansyList()
    vacs_list.import_vacansy_list(temp_vacs_list)

    top_n = int(input("Введите сколько топ-вакансий по зарплате Вам показать: "))
    print(f'Вывожу тор-{top_n} вакансий.\n')
    print(vacs_list.top_vacs(top_n))

    # Производим запись списка вакансий в файл
    vacs_file = VacansyFile()
    vacs_file.import_vacansy_list(temp_vacs_list)
    vacs_file.write_file()
    print(f"Список из {len(temp_vacs_list)} вакансий успешно записан в файл!")


if __name__ == "__main__":
    main_func()
