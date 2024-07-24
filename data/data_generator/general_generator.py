from random import randint

from faker import Faker


def generate_random_full_name() -> str:
    fake = Faker()
    full_name = fake.name()
    return full_name


def generate_random_email() -> str:
    fake = Faker()
    email = fake.email()
    return email


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
