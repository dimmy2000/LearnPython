import time
from sqlalchemy.sql import func

from db import db_session
from models import Company, Employee, Project, ProjectEmployee


def company_projects_employees(company_name):
    query = Project.query.join(
        Project.company, Project.employees
    ).filter(Company.name == company_name)

    for project in query:
        print('-' * 80)
        print(project.name)
        for employee in project.employees:
            delta = (employee.date_end - employee.date_start).days
            print(f"{employee.employee.name} -- {delta}")


def projects_time_total(company_name):
    query = db_session.query(
        Project.name, func.sum(ProjectEmployee.date_end - ProjectEmployee.date_start)
    ).join(
        Project.company, Project.employees
    ).filter(Company.name == company_name).group_by(Project.name)

    for project_name, delta in query:
        print(f'{project_name} -- {delta}')


def project_employees_time_total(company_name):
    query = db_session.query(
        Project.name,
        Employee.name,
        func.sum(ProjectEmployee.date_end - ProjectEmployee.date_start)
    ).join(
        Project.company, Project.employees, ProjectEmployee.employee
    ).filter(Company.name == company_name).group_by(Project.name, Employee.name)

    for project_name, employee_name, delta in query:
        print(f'{project_name} -- {employee_name} -- {delta}')


if __name__ == '__main__':
    # company_projects_employees("Вайлдберриз")
    # projects_time_total("Вайлдберриз")
    project_employees_time_total("Вайлдберриз")
