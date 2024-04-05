from abc import ABC, abstractmethod
import requests
import json


class Vacancy(ABC):

    @abstractmethod
    def call_to_api(self):
        pass


class VacancyApi(Vacancy):

    def __init__(self, name, id_area, salary, true_salary):
        self.__name = name
        self.__area = id_area
        self.__salary = salary
        self.__true_salary = true_salary

    def call_to_api(self):
        """Обращается к сайту hh.ru и возвращает ответ по заданным запросам"""
        req = requests.get('https://api.hh.ru/vacancies', params={'text': {self.__name},
                                                                  'area': {self.__area},
                                                                  'only_with_salary': {self.__true_salary},
                                                                  'salary': {self.__salary},
                                                                  'per_page': '100'})
        vacancy_json = req.json()
        return vacancy_json

    @staticmethod
    def to_json(file):
        """Записывает полученные с сайта данные в JSON-файл"""
        with open("data/vacancy.txt", 'w') as f:
            json.dump(file, f, indent=2, ensure_ascii=False)

