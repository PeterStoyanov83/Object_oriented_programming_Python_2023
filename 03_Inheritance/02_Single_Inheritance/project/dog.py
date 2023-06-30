from project.animal import Animal


class Dog(Animal):
    def bark(self) -> str:
        return "barking..."


dog = Dog()
print(dog.eat())
print(dog.bark())