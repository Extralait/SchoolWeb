
import pandas as pd
import re
import json

from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self,*args,**kwargs):
        speciality_dict = {
            'Фармация': 19,
            'Медицинская биохимия': 21,
            'Прикладная математика и информатика': 44,
            'Прикладная математика': 43,
            'Математика и компьютерные науки': 42,
            'Математическое обеспечение и администрирование информационных систем': 62,
            'Физика': 61,
            'Химия': 41,
            'Геология': 40,
            'Экология и природопользование': 60,
            'Биология': 38,
            'Архитектура': 37,
            'Дизайн архитектурной среды': 59,
            'Строительство': 36,
            'Строительство уникальных зданий и сооружений': 35,
            'Информационные системы и технологии': 58,
            'Прикладная информатика': 34,
            'Программная инженерия': 33,
            'Информационная безопасность': 32,
            'Компьютерная безопасность': 57,
            'Инфокоммуникационные технологии и системы связи': 31,
            'Электроника и наноэлектроника': 30,
            'Электроэнергетика и электротехника': 56,
            'Машиностроение': 29,
            'Автоматизация технологических процессов и производств': 28,
            'Мехатроника и робототехника': 55,
            'Химическая технология': 27,
            'Нефтегазовое дело': 26,
            'Землеустройство и кадастры': 24,
            'Прикладная геодезия': 23,
            'Технология транспортных процессов': 22,
            'Кораблестроение, океанотехника и системотехника объектов морской инфраструктуры': 53,
            'Инноватика': 52,
            'Психология': 50,
            'Конфликтология': 18,
            'Экономика': 17,
            'Менеджмент': 16,
            'Экономическая безопасность': 49,
            'Социология': 15,
            'Медицинская биофизика':51,
            'Лечебное дело':20,
            'Биотехнология':54,
            'Юриспруденция': 14,
            'Зарубежное регионоведение': 48,
            'Политология': 13,
            'Международные отношения': 47,
            'Реклама и связи с общественностью': 46,
            'Журналистика': 12,
            'Туризм': 11,
            'Гостиничное дело': 10,
            'Специальное (дефектологическое) образование': 9,
            'Педагогическое образование (Русский язык как иностранный)': 8,
            'Педагогическое образование (с двумя профилями подготовки) (Информационные технологии и математика)': 7,
            'Педагогическое образование (с двумя профилями подготовки) (Иностранный (английский)  язык и иностранный (китайский) язык)': 6,
            'Педагогическое образование (с двумя профилями подготовки) (Иностранный (английский)  язык и иностранный (корейский) язык)': 5,
            'Педагогическое образование (с двумя профилями подготовки) (История и обществознание)': 4,
            'Педагогическое образование (с двумя профилями подготовки) (Начальное образование и профиль по выбору (логопедия, английский язык, информатика)': 45,
            'Филология (иностранный язык)': 2,
            'Филология (русский язык)': 69,
            'Лингвистика': 68,
            'Фундаментальная и прикладная лингвистика': 67,
            'Перевод и переводоведение': 66,
            'История': 65,
            'Философия': 1,
            'Теология': 3,
            'Физическая культура': 70,
            'Дизайн': 64,
            'Востоковедение и африканистика': 63
        }

        data = pd.read_csv('data_dir/data.csv', sep=';', encoding='utf-8')
        data = data.loc[:, 'pk':'Учебный план'].fillna('')

        full_json = []

        for line in data.iterrows():
            pk = int(line[1]['pk'])
            name = line[1]['Специальность'].strip().replace('\n',' ')
            school = line[1]['Школа'].strip()
            print(school)
            number = line[1]['Код специальности'].strip()
            place = int(line[1]['Количество бюджетных мест']) if line[1]['Количество бюджетных мест'] else 0
            price = int(line[1]['Стоимость обучения']) if line[1]['Стоимость обучения'] else 0

            subjects = []
            if line[1]['Предметы']:
                subjects_names_list = [i.strip().replace('\n',' ') for i in line[1]['Предметы'].strip().split(',')]
                # print(name, subjects_names_list)
                subjects_scores_list = [i.strip() for i in line[1]['Минимальные баллы'].strip().split(',')]
                subjects_scores_list = [int(re.search(r'\d+', s).group()) for s in subjects_scores_list]
                # print(name, subjects_names_list,subjects_scores_list)

                for i in range(len(subjects_scores_list)):
                    subjects.append({'name': subjects_names_list[i],
                                     'score': subjects_scores_list[i]})

            work = []
            work_names_list = [i.strip() for i in line[1]['Трудоустройство'].strip().split('$') if i]
            work_description_list = [i.strip() for i in line[1]['Описание трудоустройства'].strip().split('$') if i]
            for i in range(len(work_names_list)):
                try:
                    work.append({'name': work_names_list[i],
                                 'score': work_description_list[i]})
                except IndexError:break

            practice = []
            practice_names_list = [i.strip() for i in line[1]['Практика'].strip().split('$') if i]
            practice_description_list = [i.strip() for i in line[1]['Описание практики'].strip().split('$') if i]
            for i in range(len(practice_names_list)):
                try:
                    practice.append({'name': practice_names_list[i],
                                     'score': practice_description_list[i]})
                except IndexError:break

            internship = []
            internship_names_list = [i.strip() for i in line[1]['Стажировка'].strip().split('$') if i]
            internship_description_list = [i.strip() for i in line[1]['Описание стажировки'].strip().split('$') if i]
            for i in range(len(internship_names_list)):
                try:
                    internship.append({'name': internship_names_list[i],
                                       'score': internship_description_list[i]})
                except IndexError:break

            passing_scores = [0] * 5
            passing_scores_str_list = line[1]['Проходные баллы прошлых лет'].split(',')
            if len(passing_scores_str_list) == 5:
                for i in range(5):
                    passing_scores[i] = int(passing_scores_str_list[i])

            main_disciplines = [i.strip() for i in line[1]['Ключевые дисциплины'].split('$') if i]
            other = line[1]['Дополнительные возможности'].strip()

            offer=[]
            offer_list = [i.strip() for i in line[1]['Смежная специальность'].strip().split('$') if i]
            if offer_list:
                for i in offer_list:
                    offer.append(speciality_dict[i])

            org_detail = line[1]['Описание специальностей'].strip()
            plan = line[1]['Учебный план'].strip()
            line_dict = {
                'model': 'api.Organization',
                'pk': pk,
                'fields': {
                    'name': name,
                    "school": school,
                    "number": number,
                    "place": place,
                    "price": price,
                    "jsons": {
                        "subjects": subjects,
                        "work": work,
                        "practice": practice,
                        "internship": internship,
                        "passing_scores": passing_scores,
                        "main_disciplines": main_disciplines,
                        "other": other
                    },
                    "logo": f"org_logo/{pk}.png",
                    "event": None,
                    "best_students": [],
                    "offer": offer,
                    "video_link": None,
                    "org_detail": org_detail,
                    "plan": plan
                }
            }
            full_json.append(line_dict)

        with open('fixtures/data.json', 'w', encoding='utf-8') as f:
            json.dump(full_json, f,indent=2, ensure_ascii=False)



