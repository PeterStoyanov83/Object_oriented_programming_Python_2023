from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        if not brand.strip():
            raise ValueError("Brand cannot be empty!")
        if not model.strip():
            raise ValueError("Model cannot be empty!")
        if not license_plate_number.strip():
            raise ValueError("License plate number is required!")

        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        self.is_damaged = not self.is_damaged

    def __str__(self):
        status = "OK" if not self.is_damaged else "Damaged"
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery: " \
               f"{self.battery_level}% Status: {status}"
