from abc import ABC, abstractmethod
import datetime
class Vehicle:
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate
        self.__owner_name = owner_name
    def get_license_plate(self):
        return self.__license_plate
    def set_license_plate(self, plate):
        self.__license_plate = plate
    def get_owner_name(self):
        return self.__owner_name
    def set_owner_name(self, name):
        self.__owner_name = name
    def display(self):
        print(f"Vehicle - Owner: {self.__owner_name}, Plate: {self.__license_plate}")
    def calculate_parking_fee(self, hours):
        raise NotImplementedError
class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required=True):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required
    def display(self):
        print(f"Bike - Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Helmet: {self.helmet_required}")
    def calculate_parking_fee(self, hours):
        return 20 * hours
class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats
    def display(self):
        print(f"Car - Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Seats: {self.seats}")
    def calculate_parking_fee(self, hours):
        return 50 * hours
class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel_drive=True):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive
    def display(self):
        print(f"SUV - Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, 4WD: {self.four_wheel_drive}")
    def calculate_parking_fee(self, hours):
        return 70 * hours
class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, max_load_capacity=10000):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity = max_load_capacity
    def display(self):
        print(f"Truck - Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Max Load: {self.max_load_capacity}kg")
    def calculate_parking_fee(self, hours):
        return 100 * hours
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.__size = size
        self.__occupied = False
        self.__vehicle = None
        self.__start_time = None
    def get_status(self):
        return "Occupied" if self.__occupied else "Free"
    def assign_vehicle(self, vehicle):
        if not self.__occupied:
            if isinstance(vehicle, Bike) and self.__size in ['S', 'M', 'L', 'XL']:
                pass
            elif isinstance(vehicle, Car) and self.__size in ['M', 'L', 'XL']:
                pass
            elif isinstance(vehicle, SUV) and self.__size in ['L', 'XL']:
                pass
            elif isinstance(vehicle, Truck) and self.__size in ['XL']:
                pass
            else:
                print(f" Vehicle {vehicle.get_license_plate()} cannot fit in Spot {self.spot_id} ({self.__size})")
                return False
            self.__vehicle = vehicle
            self.__occupied = True
            self.__start_time = datetime.datetime.now()
            print(f" Vehicle {vehicle.get_license_plate()} parked at Spot {self.spot_id}")
            return True
        else:
            print(f" Spot {self.spot_id} is already occupied")
            return False
    def remove_vehicle(self):
        if self.__occupied:
            end_time = datetime.datetime.now()
            hours = (end_time - self.__start_time).seconds // 3600 + 1
            fee = self.__vehicle.calculate_parking_fee(hours)
            vehicle = self.__vehicle
            print(f"Vehicle {vehicle.get_license_plate()} removed from Spot {self.spot_id}. Hours: {hours}, Fee: ₹{fee}")
            self.__vehicle = None
            self.__occupied = False
            self.__start_time = None
            return fee
        else:
            print(f" Spot {self.spot_id} is already empty")
            return 0
class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []
    def add_spot(self, spot):
        self.spots.append(spot)
    def show_spots(self):
        print(f"--- Parking Lot: {self.name} ---")
        for spot in self.spots:
            print(f"Spot {spot.spot_id} ({spot._ParkingSpot__size}) → {spot.get_status()}")
    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.get_status() == "Free":
                if spot.assign_vehicle(vehicle):
                    return True
        print(" No suitable spot available")
        return False
    def unpark_vehicle(self, vehicle, payment_method):
        for spot in self.spots:
            if spot._ParkingSpot__vehicle == vehicle:
                fee = spot.remove_vehicle()
                if fee > 0:
                    payment_method.process_payment(fee)
                return True
        print(" Vehicle not found in lot")
        return False
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CashPayment(Payment):
    def process_payment(self, amount):
        print(f" Paid ₹{amount} in Cash")
class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Card")
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f" Paid ₹{amount} via UPI")
if __name__ == "__main__":
    bike = Bike("AP01BK1234", "Ravi")
    car = Car("TS09CR5678", "Priya", 5)
    suv = SUV("MH12SU9012", "Amit")
    truck = Truck("DL04TR3456", "Kiran", 20000)
    vehicles = [bike, car, suv, truck]
    print("\n--- Vehicle Details ---")
    for v in vehicles:
        v.display()
    lot = ParkingLot("City Center Lot")
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "L"))
    lot.add_spot(ParkingSpot(4, "XL"))
    lot.show_spots()
    print("\n--- Parking Vehicles ---")
    for v in vehicles:
        lot.park_vehicle(v)
    lot.show_spots()
    print("\n--- Unparking Vehicles ---")
    lot.unpark_vehicle(bike, CashPayment())
    lot.unpark_vehicle(car, CardPayment())
    lot.unpark_vehicle(suv, UPIPayment())
    lot.unpark_vehicle(truck, CashPayment())
    lot.show_spots()
