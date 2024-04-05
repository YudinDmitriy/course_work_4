import json


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
        try:
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
        except Exception:
            n = 4
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
