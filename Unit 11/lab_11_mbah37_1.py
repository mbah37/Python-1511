# Moustapha Bah
# 11/06/2025
# function for inputting a rotating angle(degrees) and normalize it by removing 
# unnecessary full 360° rotations 

def normal_angle(degrees):
    '''This function takes an angle in degrees and normalizes it to be within 
    the range of 0 to 360 degrees.
    
    Returns the normalized angle if the input is valid
    otherwise returns None for invalid input.
    '''
    try:
        degrees = float(degrees)
    except (ValueError, TypeError):
        print("Invalid input: Please enter a numeric value for degrees.")
        return None    
    else:
        rotating_angle = degrees % 360
        return rotating_angle



