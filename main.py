from application import salary
from application.db import people
import datetime


if __name__ == "__main__":
    print(datetime.date.today())
    salary.calculate_salary()
    people.get_employees()
