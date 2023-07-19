from typing import List
from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = self.__initialize_photos()
        self.current_row_index = 0  # acessing 1st elment in the matrix

    def __initialize_photos(self) -> List[List[str]]:
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def _from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        if len(self.photos[self.current_row_index]) == 4:
            self.current_row_index += 1
        try:

            self.photos[self.current_row_index].append(label)
            return f"{label} photo added successfully on page " \
                   f"{self.current_row_index + 1} " \
                   f"slot {len(self.photos[self.current_row_index])}"
        except IndexError:
            return "No more free slots"

    def display(self):
        pass


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))

print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
