from data.data import Person
from faker import Faker # библ faker class Faker

faker_ru = Faker("ru_Ru")

def generated_person():
    yield Person( # класс персон из data.py
        full_name=faker_ru.first_name()+ " " +faker_ru.last_name()+ " " +faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )