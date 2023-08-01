from abc import ABC, abstractmethod


class Supply(ABC):
    def __init__(self, name: str, energy: int):
        # validate the ma,e and the energy

        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name__

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be an empty string.")
        self.name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value < 0:
            return ValueError("Energy cannot be less than zero.")
        self.__energy = value


    @abstractmethod
    def details(self):
        ...
