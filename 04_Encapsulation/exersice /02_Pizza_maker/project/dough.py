class Dough:
    def __init__(self, type_flower: str, baking_technique: str, weight: str) -> None:
        self.type_flower = type_flower
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self) -> str:
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, value: str) -> None:
        if value == "":
            raise ValueError("The flour type cannot be an empty string")
        self.__flour_type = value

