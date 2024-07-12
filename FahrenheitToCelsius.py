#Fahrenheit to celsius and opposite
from colorama import Fore, Style
counter = 1


def choose(list_operations):
        num0 = 1
        for operation in list_operations:
            print(Fore.YELLOW + f"[{num0}. {operation}]" + Style.RESET_ALL)
            num0 += 1
        
        while True:
            choice = input("\nPlease choose operation: ")
            if choice == "1" or choice == "2":
                return int(choice)
            else:
                print(Fore.RED + "Error: You must enter from displayed numbers! Enter again..." + Style.RESET_ALL)

def enter_value():
    while True:
        value = input("Please enter value: ")
        if value.isnumeric():
            return float(value)
        else:
            print(Fore.RED + "Error: You must enter a number! Enter again:\n" + Style.RESET_ALL)

def operation(value, choice):
    if choice == 1:
        result = round((value * 1.8) + 32, 2)
        unit = "F"
    else:
        result = round((value - 32) * 5 / 9, 2)
        unit = "C"
    return result, unit

def ending(counter):
    end = input("Would you like to repeat the application?(Y/n) ")
    end = end.upper()
    if end == "N":
        print("\nGoodBye!\n")
        underscore()
        close = True
    elif end == "Y":
        counter += 1
        close = False
    else:
        print(Fore.RED + "Error: wrong selection!" + Style.RESET_ALL)
        ending(counter)
        close = False
    return close, counter

def underscore():
    for i in range(0, 48):
        print("_", end="")

def main():
    list_operations = ["Celsius to Fahrenheit","Fahrenheit to Celsius"]
    counter = 1
    while True:
        underscore()
        if not counter == 1:
            print(f"\nOperation number ({counter})")
        else:
            print("\nWelcome to Fahrenheit/Celsius converter!\n")

        choice = choose(list_operations)
        value = enter_value()
        result, unit = operation(value, choice)
        print(Fore.GREEN + f"\nResult: {result} °{unit}.\n" + Style.RESET_ALL)
        close, counter = ending(counter)
        if close == True:
            break


if __name__ == "__main__":
    main()
    