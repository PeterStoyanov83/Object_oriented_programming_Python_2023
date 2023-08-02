class User:
    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        if not first_name.strip():
            raise ValueError("First name cannot be empty!")
        if not last_name.strip():
            raise ValueError("Last name cannot be empty!")
        if not driving_license_number.strip():
            raise ValueError("Driving license number is required!")
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = 0.0
        self.is_blocked = False

    def increase_rating(self):
        self.rating += 0.5
        if self.rating > 10.0:
            self.rating = 10.0

    def decrease_rating(self):
        self.rating -= 2.0
        if self.rating < 0.0:
            self.rating = 0.0
            self.is_blocked = True

    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license:" \
               f" {self.driving_license_number} Rating: {self.rating}"
