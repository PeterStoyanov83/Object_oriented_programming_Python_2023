class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        pages = (photos_count + 3) // 4
        return cls(pages)

    def add_photo(self, label: str) -> str:
        for page_number, page in enumerate(self.photos, start=1):
            if len(page) < 4:
                slot_number = len(page) + 1
                page.append(label)
                return f"{label} photo added successfully on page {page_number} slot {slot_number}"
        return "No more free slots"

    def display(self) -> str:
        res = ""
        for page in self.photos:
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
