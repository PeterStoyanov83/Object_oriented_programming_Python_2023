class Person:
    def __init__(self, name, age):
        if not name:
            raise Exception("cannot make an instance of class with no name")
        self.name = name
        self.age = age

    def say_name(self):
        return f"hello my name {self.name}"


class Employee(Person):
    def __init__(self, name, age, sec_number, ):
        super.__init__(name, age)
        self.sec_number = sec_number


class Unemployed(Person):
    pass


class Student(Person):
    pass


class Teacher:
    def __init__(self, name, sec_number, children):
        self.name = name
        self.sec_number = sec_number
        self.children = children


p = Person("a", 13)
e = Employee("a", 13, 1234)
print(e.say_name())
