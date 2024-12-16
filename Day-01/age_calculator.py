# Age Calculator
from datetime import datetime

# User Input
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year (e.g., 2000): "))

# Calculate Age
current_year = datetime.now().year
age = current_year - birth_year

# Output Result
print(f"Hello, {name}! You are {age} years old.")
