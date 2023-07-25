# Creating the Person class

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


# Creating the Group class

class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self):
        members = ", ".join([str(person) for person in self.people])
        return f"Group {self.name} with members {members}"

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.people):
            result = f"Person {self.index}: {self.people[self.index]}"
            self.index += 1
            return result
        raise StopIteration


person1 = Person("John", "Doe")
person2 = Person("Jane", "Smith")
person3 = Person("Emily", "Johnson")
person4 = Person("Michael", "Williams")

print(person1)
print(person2)

person5 = person1 + person2
print(person5)

group1 = Group("Group1", [person1, person2])
group2 = Group("Group2", [person3, person4])

print(f"group1{group1}\ngroup2{group2}")