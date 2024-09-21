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
    path = rf"C:\Users\48788\PycharmProjects\python_selenium_portfolio\generated_file\{random.randint(0,999)}.txt"
    file = open(path, 'w+')
    file.write(f"{generate_random_permanent_address()}")
    file.close()
    return path