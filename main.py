from src.VacancyApi import VacancyApi
from src.VacancyOutput import VacancyOutput
from src.user_input import UserInput

user_input = UserInput.user_input()


hh_vacancy = VacancyApi(user_input[0], user_input[1], user_input[2], user_input[3])
hh_vacancy.to_json(hh_vacancy.call_to_api())

hh_out_vacancy = VacancyOutput()
hh_out_vacancy.fin_vac(hh_out_vacancy.sort_vacancy(hh_out_vacancy.json_text()))
