"""This module provides a simple function to add two numbers."""

def add(number1: int, number2: int) -> int:
    """Return the sum of two numbers."""
    return number1 + number2

NUM1 = 4  # Constant variable
NUM2 = 5  # Constant variable

TOTAL = add(NUM1, NUM2)  # Store the sum of NUM1 and NUM2

# Print the result using an f-string
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
