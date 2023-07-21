from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def work(self):
        ...


class Employee(Person):
    def work(self):
        print("working...")


class Boss(Person):
    def work(self):
        print("taking risks...")


        