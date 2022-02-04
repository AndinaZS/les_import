from application.salary import *
from db.people import *
from datetime import *


if __name__ == '__main__':
    print(datetime.date(datetime.today()))
    calculate_salary()
    get_employees()

