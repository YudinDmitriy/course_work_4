from abc import ABC, abstractmethod
import requests
import json


class Vacancy(ABC):

    @abstractmethod
    def call_to_api(self):
        pass


class VacancyApi(Vacancy):

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
        """Обращается к сайту hh.ru и возвращает ответ по заданным запросам"""
        req = requests.get('https://api.hh.ru/vacancies', params={'text': {self.name},
                                                                  'area': {self.area},
                                                                  'only_with_salary': {self.true_salary},
                                                                  'salary': {self.salary},
                                                                  'per_page': '100'})
        vacancy_json = req.json()
        return vacancy_json

    @staticmethod
    def to_json(file):
        """Записывает полученные с сайта данные в JSON-файл"""
        with open("data/vacancy.txt", 'w') as f:
            json.dump(file, f, indent=2, ensure_ascii=False)


class VacancyOutput:

    @staticmethod
    def json_text():
        """Открывает json-файл и возвращает словарь с вакансиями имеющими зарплату от ..."""

        with open("data/vacancy.txt", 'r') as file:
            fcc_data = json.load(file)
            vacancy_with_from = {}
            c = 0
            for f in fcc_data['items']:
                salary_from = f['salary']['from']
                if isinstance(salary_from, int):
                    c += 1
                    vacancy_with_from[f'vacancy{c}'] = [f['name'], f['salary']['from'],
                                                        f['area']['name'], f['alternate_url'],
                                                        f['snippet']['requirement'], f['snippet']['responsibility']]
                else:
                    continue
            return vacancy_with_from

    @staticmethod
    def sort_vacancy(dict_vac):
        """Получает dict, возвращает топ N вакансий по зарплате"""
        n = int(input('Количество выводимых вакансий: '))
        sorted_vac = sorted(dict_vac.items(), key=lambda item: item[1][1], reverse=True)
        fin_vac = []
        for c in sorted_vac:
            fin_vac.append(f'\nДолжность: {c[1][0]}\n'
                           f'Город: {c[1][2]}\n'
                           f'Зарплата от {c[1][1]} руб\n'
                           f'Требования: {c[1][4]}\n'
                           f'Ответственность: {c[1][5]}\n'
                           f'Ссылка на hh.ru: {c[1][3]}\n')
        return fin_vac[:n]

    @staticmethod
    def fin_vac(vac):
        for a in vac:
            print(a)
