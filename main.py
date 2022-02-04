from application.salary import calculate_salary
from db.people import get_employees
from datetime import datetime


if __name__ == '__main__':
    print(datetime.date(datetime.today()))
    calculate_salary()
    get_employees()

