#Fahrenheit to celsius and opposite
from colorama import Fore, Style
counter = 1

def Celsius_to_Fahrenheit(temperature):
    return round((temperature * 1.8) + 32, 2)
def Fahrenheit_to_Celsius(temperature):
    return round((temperature - 32) * 5 / 9, 2)

while True:

    print(f"Operation number ({counter})")
    list_operations = ["Celsius to Fahrenheit","Fahrenheit to Celsius"]

    num0 = 1
    for operation in list_operations:
        print(f"[{num0}. {operation}]")
        num0 = num0 + 1


    while True:
        choose = input("Select number of operation:\n")

        if choose == "1":
            choosed = "F"
            break
        elif choose == "2":
            choosed = "C"
            break
        else:
            print(Fore.RED + "Error: You must enter from displayed numbers! Enter again:\n" + Style.RESET_ALL)

    while True:
        temperature = input("Please enter value:\n")

        if temperature.isnumeric():
            temperature = float(temperature)
            break
        else:
            print(Fore.RED + "Error: You must enter a number! Enter again:\n" + Style.RESET_ALL)


    if choose == 1:
        result = Celsius_to_Fahrenheit(temperature)
    else:
        result = Fahrenheit_to_Celsius(temperature)

    print(f"\nResult: {result}° {choosed}.\n")


    end = input("Would you like to do the operation again?(Y/N)")
    end = end.upper()

    if end == "N":
        break
    else:
        counter = counter + 1
    