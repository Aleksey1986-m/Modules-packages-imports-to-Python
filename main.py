from salary import calculate_salary
from people import get_employees
from datetime import date

today = date.today()

if __name__ == '__main__':
    print('Current date =', today)
    calculate_salary()
    get_employees()
