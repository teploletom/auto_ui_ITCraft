from dataclasses import dataclass


@dataclass #предназначены для хранения данных
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: int = None
    email: str = None
    current_address: str = None
    permanent_address: str = None

