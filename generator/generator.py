import random

from data.data import Person
from faker import Faker # библ faker class Faker

faker_ru = Faker("ru_Ru")

def generated_person():
    yield Person( # класс персон из data.py
        full_name=faker_ru.first_name()+ " " +faker_ru.last_name()+ " " +faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )