import copy


class Person:
    def __init__(self, position):
        self.position = position


class FreePerson(Person):
    def __init__(self, position):
        super().__init__(position)

    def walk(self, direction, dist):
        if direction == "north":
            self.position[1] += dist
        elif direction == "east":
            self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False


prisoner = Prisoner()
print("The prisoner is trying to walk north by 10 and east by -3.")

try:
    prisoner.walk("north", 10)
    prisoner.walk("east", -3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")
