#1. we want to update pip and install pytest in our virtual environment
def say_hello(name: str):
  """Simple print greeting with name

  Args:
      name (str): The name of the user
  """
  print(f'Hello {name}')


def is_even(number):
    """
    Returns True if the number is even, False otherwise.
    """
    
    return number % 2 == 0
    

def divide(x, y):
    """
    Divides two numbers and returns the result.

    Args:
      x: The numerator (number to be divided).
      y: The denominator (number to divide by).

    Raises:
      ZeroDivisionError: If y is zero
    
    Returns:
      The result of dividing x by y.
    """
    
    if y == 0:
      raise ZeroDivisionError
      
    return x / y



def calculate_discount(price, discount_percentage):
  """
  Calculates the discounted price given the original price and discount percentage.
  Handles potential TypeError and ValueError exceptions.
  """
  
    
  # Convert discount_percentage to a decimal
  discount_decimal = discount_percentage / 100  
  # Calculate the discount amount
  discount_amount = price * discount_decimal  

  # Calculate the final price
  final_price = price - discount_amount  
  return final_price

def get_max_in_list(numbers):
  """Returns the maximum value in a list.
  Raises ValueError if the list is empty.
  """
  if numbers:
      return max(numbers)
  else:
      raise ValueError("List cannot be empty.")
  




