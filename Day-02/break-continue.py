for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at:", i)
        break  # Exit the loop when i equals 5
    print("Number:", i)

# Continue
    
for i in range(1, 6):
    if i == 3:
        print("Skipping the number:", i)
        continue  # Skip printing when i equals 3
    print("Number:", i)