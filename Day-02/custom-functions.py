# Example 1: Simple Function
# Defining a function to greet
def greet_user(name):
    print("Hello,", name)

# Calling the function
greet_user("Raghul")
greet_user("CareerPod")

#Example 2: Function with Return Value
# Function to add two numbers
def add_numbers(a, b):
    return a + b
# Calling the function
result = add_numbers(5, 7)
print("Sum:", result)


#Example 3: Function with Default Parameters
# Function with a default value for a parameter
def greet_user(name="Guest"):
    print("Hello,", name)
# Calling the function
greet_user()  # Uses default value
greet_user("Raghul")  # Overrides default value


#Example 4: Function with Multiple Return Values
# Function to return multiple results
def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val, diff_val
# Calling the function
s, d = calculate(10, 5)
print("Sum:", s)
print("Difference:", d)