# Домашнее задание к лекции 1. «Import. Module. Package» Разработать структуру программы «Бухгалтерия»

from package_selary.salary import calculate_salary
from packege_people.people import get_employees
from datetime import date

today = date.today()

if __name__ == '__main__':
    print('Current date =', today)
    calculate_salary()
    get_employees()
