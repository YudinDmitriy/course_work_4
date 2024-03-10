from abc import ABC, abstractmethod
import requests
import json


class Vacancy(ABC):

    @abstractmethod
    def call_to_api(self):
        pass


class Vacancy_api(Vacancy):

    def __init__(self):
        area = input('Введите город: ')
        req_area = requests.get('https://api.hh.ru/suggests/areas', params={'text': area})
        test3 = req_area.json()
        id_area = test3['items'][0]['id']
        self.name = input('Введите название вакансии: ')
        self.area = id_area
        self.salary = input('Введите минимальную зарплату: ')
        self.true_salary = True

    def call_to_api(self):
        req = requests.get('https://api.hh.ru/vacancies', params={'text': {self.name},
                                                                  'area': {self.area},
                                                                  'only_with_salary': {self.true_salary},
                                                                  'salary': {self.salary},
                                                                  'per_page': '100'})
        vacancy_json = req.json()
        return vacancy_json

    @staticmethod
    def to_json(file):
        with open("../data/vacancy.txt", 'w') as f:
            json.dump(file, f, indent=2, ensure_ascii=False)


