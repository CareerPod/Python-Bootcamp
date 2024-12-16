print("Simple Calculator")
print("Select Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")

choice = input("Enter the number corresponding to the operation (1/2/3/4/5): ")

if choice in ["1", "2", "3", "4", "5"]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if choice == "1":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == "5":
        result = num1 % num2
        print(f"The result of {num1} % {num2} is: {result}")
else:
    print("Invalid choice. Please select a number between 1 and 5.")
