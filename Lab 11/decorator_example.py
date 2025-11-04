# format for creating a decorator
# define the decorator function pass in a general function call 
# define an internal function that will wrap around the function that 
# you are adding functionality to 
# add args and kwargs as parameters incase the original function needs them
# perform you additonal functionality before, during, and/or after
# assign result to the function call 
# return result to the wrapper
# return wrapper
# Now you can call the function using the @ symbol right before the function 
# you want to decorate

import time

def decorator(func):
    """
    This decorator adds additional functionality.
    """
    def wrapper(*args, **kwargs):
        print("Doing something before function call")
        result = func(*args, **kwargs)
        print("Doing something after function call")
        return result
    return wrapper

def timer(func):
    """
    This decorator adds additional functionality for time.
    """
    



def prepare_gift(gift_name):
    """
    This function represents the preparation of a gift.
    """
    time.sleep(1)
    print(f"Preparing a {gift_name}...")
    return f"A beautifully prepared {gift_name}"

# Using the decorated function
gift = prepare_gift("teddy bear")
print(gift)