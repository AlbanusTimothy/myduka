# OOP TASK 
# 1.Create a Car Class
# Have the following attributes
# - brand - model - year -fuel_capcity - fuel_level -is_running(boolen value)
# Have the methods
# - start()
# - stop()
# - refuel()
# - drive()
# - display_car_info()

class Car:
    def __init__(self, brand, model, year, fuel_capacity):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0
        self.is_running = False

    def start(self):
        if self.fuel_level > 0:
            self.is_running = True
            return "Car started."
        return "Cannot start. No fuel!"

    def stop(self):
        if self.is_running:
            self.is_running = False
            return "Car stopped."
        return "Car is already off."

    def refuel(self, amount):
        if amount <= 0:
            return "Invalid fuel amount."

        max_addable = self.fuel_capacity - self.fuel_level  # remaining space in tank

        if amount > max_addable:
            return f"Cannot add {amount}L. You can only add {max_addable}L to fill the tank."

        self.fuel_level += amount
        return f"Added {amount}L of fuel. Current fuel: {self.fuel_level}L"

    def drive(self, distance):
        if not self.is_running:
            return "Start the car first."

        fuel_needed = distance * 0.1 #car drives 1km with 0.1L
        max_distance = self.fuel_level / 0.1  # max distance possible with current fuel

        if fuel_needed > self.fuel_level:
            return (
                f"Not enough fuel for {distance} km. "
                f"With current fuel, you can only cover {max_distance:.1f} km. "
                f"Refuel after that."
            )

        self.fuel_level -= fuel_needed
        return f"Drove {distance} km. Fuel remaining: {self.fuel_level:.1f}L"

    def __str__(self):
        return (
            f"Car Info:\n"
            f"Brand: {self.brand}\n"
            f"Model: {self.model}\n"
            f"Year: {self.year}\n"
            f"Fuel: {self.fuel_level}/{self.fuel_capacity}L\n"
            f"Running: {self.is_running}"
        )


# -------Tryyyyyyyyyyyyyyyyyyyyyyyyyy itttttttttttttttttttttttttttt----
# Create my  machines
car1 = Car("BMW", "7 Series", 2023, 80)
car2 = Car("Range Rover", "Sport", 2022, 90)
car3 = Car("Audi", "A7", 2021, 70)
car4 = Car("Bentley", "Flying Spur", 2023, 95)
car5 = Car("Porsche", "Panamera", 2022, 85)

# Refuel the cars
print(car1.refuel(50))
print(car2.refuel(60))
print(car3.refuel(40))
print(car4.refuel(80))
print(car5.refuel(70))

# Start the cars
print(car1.start())
print(car2.start())
print(car3.start())
print(car4.start())
print(car5.start())

# Drive the cars
print(car1.drive(300))  # 300 km trip
print(car2.drive(500))  # 500 km trip
print(car3.drive(200))  # 200 km trip
print(car4.drive(900))  # 900 km trip, should show limitation
print(car5.drive(600))  # 600 km trip, might need refuel

# Stop the cars
print(car1.stop())
print(car2.stop())
print(car3.stop())
print(car4.stop())
print(car5.stop())

# Display car info
print(car1)
print(car2)
print(car3)
print(car4)
print(car5)
