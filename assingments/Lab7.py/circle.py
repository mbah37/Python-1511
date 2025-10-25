#Moustapha Bah 10/17/25
#This module contains functions to calculate the area and circumference of a circle.

# Function to calculate the area of a circle
def get_circle_area(radius):
    import math
    area = math.pi * radius ** 2
    return area


# Function to calculate the circumference of a circle
def get_circle_circumference(radius):
    import math
    circumference = 2 * math.pi * radius
    return circumference


