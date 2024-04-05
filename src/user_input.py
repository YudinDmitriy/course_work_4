import requests


class UserInput:

    @staticmethod
    def user_input():
        try:
            area = input('Введите город: ')
            req_area = requests.get('https://api.hh.ru/suggests/areas', params={'text': area})
            area = req_area.json()
            id_area = area['items'][0]['id']
            name = input('Введите название вакансии: ')
            salary = input('Введите минимальную зарплату (если не важна укажите "0" или оставьте пустым): ')
            if salary in (0, ""):
                salary = 1
            true_salary = True
        except Exception:
            print('Указанный город не найден, результат показан по всей России')
            id_area = '113'
            name = input('Введите название вакансии: ')
            salary = input('Введите минимальную зарплату (если не важна укажите "0" или оставьте пустым): ')
            if salary in (0, ""):
                salary = 1
            true_salary = True

        return name, id_area, salary, true_salary

test = UserInput.user_input()
print(test)
# for i in test:
#     print(i)
