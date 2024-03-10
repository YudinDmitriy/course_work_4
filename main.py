from src.classes import VacancyApi, VacancyOutput

hh_vacancy = VacancyApi()
hh_vacancy.to_json(hh_vacancy.call_to_api())

hh_out_vacancy = VacancyOutput()
hh_out_vacancy.fin_vac(hh_out_vacancy.sort_vacancy(hh_out_vacancy.json_text()))
