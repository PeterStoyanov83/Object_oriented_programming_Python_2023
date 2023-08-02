from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if any(user.driving_license_number == driving_license_number for user in self.users):
            return f"{driving_license_number} has already been registered to our platform."
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."
        if any(vehicle.license_plate_number == license_plate_number for vehicle in self.vehicles):
            return f"{license_plate_number} belongs to another vehicle."
        if vehicle_type == "PassengerCar":
            new_vehicle = PassengerCar(brand, model, license_plate_number)
        else:  # vehicle_type == "CargoVan"
            new_vehicle = CargoVan(brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."
