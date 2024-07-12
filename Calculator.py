from colorama import Fore, Style


def sumarize(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    while True:
        if b != 0:
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

def perform_operation(select, num1, num2):
    if select == 1:
        return sumarize(num1, num2)
    elif select == 2:
        return substract(num1, num2)
    elif select == 3:
        return multiply(num1, num2)
    elif select == 4:
        return divide(num1, num2)
    elif select == 5:
        return exponent(num1, num2)

def list_function(list_f):
    num0 = 1
    for function in list_f:
        print(f"[{num0}. {function}]")
        num0 = num0 + 1

def choose_function():
    while True:
        selected_function = input("\nYour choose:\n> ")
        if selected_function.isnumeric() and 1 <= int(selected_function) < 6 :
            select = int(selected_function)
            break
        else:
            print(Fore.RED + "Error: You must enter printed number! Enter again:\n" + Style.RESET_ALL)
    return select

def enter_and_calculate(select):
    while True:
        num1 = input("\nEnter number a:\n> ")
        num2 = input("Enter number b:\n> ")

        if num1.isnumeric() and num2.isnumeric():
            num1 = float(num1)
            num2 = float(num2)
            break
        else:
            print(Fore.RED + "Error: At least one of entered values is not number! Enter again:\n" + Style.RESET_ALL)
    result = round(perform_operation(select, num1, num2), 3)
    return result
        


def main():
    list_f = ["Sumarize","Substract","Multiply","Divide","Exponent"]
    print(f"\nSelect number of desired operation:\n")
    list_function(list_f)
    select = choose_function()
    result = enter_and_calculate(select)
    print(f"\nYour answer is: {result}")

    while True:
        end = input(f"Would you like to continue?(Y/n)\n> ")
        if end.lower() == "y":
            main()
        elif end.lower() == "n":
            print("\nBye!\n")
            break
        else:
            print("What?!\n")

        

if __name__ == "__main__":
    main()