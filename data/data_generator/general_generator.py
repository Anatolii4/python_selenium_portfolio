from datetime import datetime
import random
from random import randint

from faker import Faker


def generate_random_full_name() -> str:
    fake = Faker()
    full_name = fake.name()
    return full_name


def generate_random_first_name() -> str:
    fake = Faker()
    first_name = fake.first_name()
    return first_name


def generate_random_last_name() -> str:
    fake = Faker()
    last_name = fake.last_name()
    return last_name


def generate_random_email() -> str:
    fake = Faker()
    email = fake.email()
    return email


def generate_random_age() -> str:
    age = random.randint(18, 65)
    return str(age)


def generate_random_salary() -> str:
    salary = random.randint(2000, 10000)
    return str(salary)


def generate_random_department() -> str:
    fake = Faker()
    while True:
        department_name = fake.job()
        if len(department_name) <= 25:
            return department_name


def generate_random_current_address() -> str:
    fake = Faker()
    current_address = fake.address()
    return current_address


def generate_random_permanent_address() -> str:
    fake = Faker()
    permanent_address = fake.address()
    return permanent_address


def choose_random_num_checkboxes():
    return randint(1, 9)


def generate_file():
    path = rf"C:\Users\48788\PycharmProjects\python_selenium_portfolio\generated_file\{random.randint(0, 999)}.txt"
    file = open(path, 'w+')
    file.write(f"{generate_random_permanent_address()}")
    file.close()
    return path


def generate_random_month_birth():
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
    return month_list[random.randint(0, 11)]


def generate_random_year_birth():
    current_year = datetime.now().year
    return random.randint(1900, current_year)


def generate_random_subject():
    subject_list = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
                    "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    return subject_list[random.randint(0, 13)]


def generate_random_state():
    state_list = ["Uttar Pradesh", "NCR", "Haryana", "Rajasthan"]
    return state_list[random.randint(0, 3)]


def choose_random_city(state: str):
    if state == "Uttar Pradesh":
        city_list = ["Agra", "Lucknow", "Merrut"]
        return city_list[random.randint(0, 2)]
    elif state == "NCR":
        city_list = ["Delhi", "Gurgaon", "Noida"]
        return city_list[random.randint(0, 2)]
    elif state == "Haryana":
        city_list = ["Karnal", "Panipat"]
        return city_list[random.randint(0, 1)]
    elif state == "Rajasthan":
        city_list = ["Jaipur", "Jaiselmer"]
        return city_list[random.randint(0, 1)]
