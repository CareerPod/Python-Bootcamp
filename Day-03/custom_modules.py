def greet():
    print("Welcome to the BootCamp")

def onepiece():
    print("Onepiece Characters ....")
    print("  ")
    chars = ["Luffy","Zoro","Nami","Sanji","Brook","Chopper","Ussop","Robin"]
    for index, char in enumerate(chars,start=1):
        print(f'{index} : {char}')