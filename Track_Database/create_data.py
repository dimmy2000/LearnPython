from datetime import date, timedelta
import csv
import random

from models import Company


def get_project_name():
    projects = ['Ребрендинг', 'Разработка CRM', 'Обслуживание 1С', 'Разработка сайта',
                'Опрос покупателей', 'Запуск колцентра', 'Модернизация wifi-сети',
                'Проведение исследований', 'Дизайн сайта', 'Разработка моб. приложения',
                'Дизайн буклетов', 'Аудит информационной безопасности',
                'Обучение сотрудников']

    return random.choice(projects)


def fake_data():
    data = []
    companies = Company.query.all()
    for company in companies:
        for employee in company.employees:
            data += fake_projects_for_employee(company.id, employee.id)
    return data


def fake_projects_for_employee(company_id, employee_id):
    projects = []
    for month in range(1, 13):
        date_start = date(2020, month, random.randint(1, 10))
        date_end = date_start + timedelta(days=random.randint(5, 15))
        project = [get_project_name(), company_id, employee_id, date_start, date_end]
        projects.append(project)
    return projects


def generate_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    generate_data(fake_data(), 'projects.csv')
