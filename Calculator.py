from colorama import Style, Fore

def sumarize(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    while True:
        if b == 0:
            print(Fore.RED + "Error: must not be null!\n" + Style.RESET_ALL)
            b = input("Enter number b:\n")
        else:
            try:
                b = float(b)
                return a / b
            except ValueError:
                print(Fore.RED + "Error: Input must be a number!\n" + Style.RESET_ALL)
                b = input("Enter number b:\n")

def exponent(a, b):
    return a ** b

def perform_operation(operation, a, b):
    if select == 1:
        return sumarize(int1, int2)
    elif select == 2:
        return substract(int1, int2)
    elif select == 3:
        return multiply(int1, int2)
    elif select == 4:
        return divide(int1, int2)
    elif select == 5:
        return exponent(int1, int2)


list_functions = ["Sumarize","Substract","Multiply","Divide","Exponent"]
print("\nSelect number of desired operation:\n")
num0 = 1

for function in list_functions:
    print(f"[{num0}. {function}]")
    num0 = num0 + 1
while True:
    selected_function = input("\nYour choose: ")
    if selected_function.isnumeric() and 1 <= int(selected_function) < 6 :
        select = int(selected_function)
        break
    else:
        print(Fore.RED + "Error: You must enter printed number! Enter again:\n" + Style.RESET_ALL)


while True:
    print("")
    num1 = input("Enter number a:\n")
    num2 = input("Enter number b:\n")

    if num1.isnumeric() and num2.isnumeric():
        int1 = float(num1)
        int2 = float(num2)
        break
    else:
        print(Fore.RED + "Error: At least one of entered values is not number! Enter again:\n" + Style.RESET_ALL)


result = round(perform_operation(select, int1, int2), 3)
print(f"\nYour answer is: {result}\n")