from a.project import Employee
from a.project import Person


class Teacher(Employee, Person):

    def teach(self):
        return "teaching..."
