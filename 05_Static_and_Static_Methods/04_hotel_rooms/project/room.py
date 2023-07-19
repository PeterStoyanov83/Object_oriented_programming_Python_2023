class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests: int = 0
        self.is_taken = False

    def take_room(self, people: int):
        if not self.is_taken and self.capacity >= people:
            self.is_taken = True
            self.guests = people

        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            if self.guests > 0:
                self.guests = 0

            self.is_taken = False
        return f"Room number {self.number} is not taken"
