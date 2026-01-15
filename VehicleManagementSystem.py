#!/usr/bin/env python
# coding: utf-8

# In[1]:


from abc import ABC, abstractmethod
import random

class Vehicle(ABC):
    def __init__(self, manufacturer, model, wheels, type_of_vehicle, seats, manufacturing_number):
        self.manufacturer = manufacturer
        self.model = model
        self.wheels = wheels
        self.type_of_vehicle = type_of_vehicle
        self.seats = seats
        self.manufacturing_number = manufacturing_number

    @abstractmethod
    def printDetails(self):
        pass

    @abstractmethod
    def checkInfo(self, **kwargs):
        pass

class Car(Vehicle):
    def __init__(self, manufacturer, model, seats, manufacturing_number):
        super().__init__(manufacturer, model, 4, "Car", seats, manufacturing_number)
        print("A car was created.")

    def printDetails(self):
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Wheels: {self.wheels}")
        print(f"Type of Vehicle: {self.type_of_vehicle}")
        print(f"Seats: {self.seats}")
        print(f"Manufacturing Number: {self.manufacturing_number}")

    def checkInfo(self, **kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {getattr(self, key) == value}")

class Truck(Vehicle):
    def __init__(self, manufacturer, model, seats, manufacturing_number):
        super().__init__(manufacturer, model, 4, "Truck", seats, manufacturing_number)
        print("A truck was created.")

    def printDetails(self):
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Wheels: {self.wheels}")
        print(f"Type of Vehicle: {self.type_of_vehicle}")
        print(f"Seats: {self.seats}")
        print(f"Manufacturing Number: {self.manufacturing_number}")

    def checkInfo(self, **kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {getattr(self, key) == value}")

class Motorcycle(Vehicle):
    def __init__(self, manufacturer, model, seats, manufacturing_number):
        super().__init__(manufacturer, model, 2, "Motorcycle", seats, manufacturing_number)
        print("A motorcycle was created.")

    def printDetails(self):
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Wheels: {self.wheels}")
        print(f"Type of Vehicle: {self.type_of_vehicle}")
        print(f"Seats: {self.seats}")
        print(f"Manufacturing Number: {self.manufacturing_number}")

    def checkInfo(self, **kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {getattr(self, key) == value}")

if __name__ == "__main__":
    manufacturers = ['Toyota', 'GM', 'Ford', 'Jeep', 'Audi']
    models = {'Car': ['X11', 'i3', 'XFCE'], 'Truck': ["Linux", "Unix", "FreeBSD"], 'Motorcycle': ["Triforce", "Mushroom", "Morphball"]}
    seats = {'Car': [2, 3, 4, 5], 'Truck': [2, 3, 4], 'Motorcycle': [1, 2]}
    total = {'Car': 0, 'Truck': 0, 'Motorcycle': 0}

    vehicles = []

    for _ in range(5):
        manufacturer = random.choice(manufacturers)
        vehicle_type = random.choice(['Car', 'Truck', 'Motorcycle'])
        model = random.choice(models[vehicle_type])
        seats_num = random.choice(seats[vehicle_type])
        total[vehicle_type] += 1
        manufacturing_number = total[vehicle_type]

        if vehicle_type == 'Car':
            vehicles.append(Car(manufacturer, model, seats_num, manufacturing_number))
        elif vehicle_type == 'Truck':
            vehicles.append(Truck(manufacturer, model, seats_num, manufacturing_number))
        elif vehicle_type == 'Motorcycle':
            vehicles.append(Motorcycle(manufacturer, model, seats_num, manufacturing_number))

    # Select one instance and test its printDetails() and checkInfo()
    selected_vehicle = random.choice(vehicles)
    print("Selected Vehicle:")
    selected_vehicle.printDetails()
    selected_vehicle.checkInfo(seats=selected_vehicle.seats)

    # Print out the total amount of each vehicle created
    print("\nTotal Vehicles Created:")
    for vehicle_type, count in total.items():
        print(f"{vehicle_type}: {count}")


# In[ ]:




