from typing import List
from a.project import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int) -> 'Hotel':
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if result is None:
                    self.guests += people
                return result
        return f"Room number {room_number} not found"

    def free_room(self, room_number: int) -> None:
        for room in self.rooms:
            if room.number == room_number:
                result = room.free_room()
                if result is None:
                    self.guests -= room.guests
                return result
        return f"Room number {room_number} not found"

    def status(self) -> str:
        free_rooms = []
        taken_rooms = []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(str(room.number))
            else:
                free_rooms.append(str(room.number))

        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms)}\n" \
               f"Taken rooms: {', '.join(taken_rooms)}"
