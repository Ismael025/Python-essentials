import math  # Importing standard library for mathematical functions

# Define the Car class
class Car:
    def __init__(self, brand, colour):
        """Constructor to specify brand and colour when creating the car object"""
        self.brand = brand
        self.colour = colour

    def display_details(self):
        """Method to display the car's details"""
        print(f"Car Brand: {self.brand}")
        print(f"Car Colour: {self.colour}")


# --- Main Program Execution ---

# 1. Model the car, specify its details, and display them
my_car = Car(brand="Toyota", colour="Red")
my_car.display_details()

print("-" * 30)

# 2. Calculate the side length of a square parking space using math.sqrt
area = 25
side_length = math.sqrt(area)  # Using Python's standard library

# Display the parking space details
print("Parking Space Area:", area, "square metres")
print(f"Required Side Length: {side_length} metres")
