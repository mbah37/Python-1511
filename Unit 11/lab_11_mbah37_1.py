# Moustapha Bah
# 11/06/2025
# function for inputting a rotating angle(degrees) and normalize it by removing 
# unnecessary full 360° rotations 

def normal_angle(degrees):
    while True: 
        try:
            degrees = float(degrees)
        except (ValueError, TypeError):
            print("Invalid input: Please enter a numeric value for degrees.")
            continue
        else:
            rotating_angle = degrees % 360
            return rotating_angle



