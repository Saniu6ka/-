import datetime

from application.salary import calculate_salary
from application_db.people import get_employees

current_date = datetime.datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print("Текущая дата:", formatted_date)

if __name__ == '__main__':
    calculate_salary()
    get_employees()
