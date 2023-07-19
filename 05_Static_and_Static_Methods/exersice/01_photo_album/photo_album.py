from typing import List, TypeVar
import math

T = TypeVar("T", bound="TrivialClass")


class PhotoAlbum:
    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: List[List[str]] = self.__initialize_photos()
        self.current_row_index = 0  # acessing 1st elment in the matrix

    def __initialize_photos(self) -> List[List[str]]:
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def _from_photos_count(cls, photos_count: int) -> T:
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str) -> str:
        if len(self.photos[self.current_row_index]) == 4:
            self.current_row_index += 1
        try:

            self.photos[self.current_row_index].append(label)
            return f"{label} photo added successfully on page " \
                   f"{self.current_row_index + 1} " \
                   f"slot {len(self.photos[self.current_row_index])}"
        except IndexError:
            return "No more free slots"

    def display(self) -> str:
        res = ""
        for page in self.photos:
            if len(page) == 0:
                res += "-" * 11 + "\n"
            else:
                res += "-" * 11 + "\n"
                res += " ".join(["[]" for _ in page]) + "\n"
        res += "-" * 11
        return res


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
