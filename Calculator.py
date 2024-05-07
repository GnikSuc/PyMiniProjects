from colorama import Style, Fore


def sumarize(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

list_functions = ["Sumarize","Substract","Multiply","Divide"]


while True:
    num1 = input("Enter number a:\n")
    num2 = input("Enter number b:\n")

    if num1.isnumeric() and num2.isnumeric():
        int1 = float(num1)
        int2 = float(num2)
        break
    else:
        print(Fore.RED + "Error: At least one of entered values is not number! Enter again:\n" + Style.RESET_ALL)

print("\nSelect number of desired operation:\n")

num0 = 1
for function in list_functions:
    print(f"[{num0}. {function}]")
    num0 = num0 + 1

while True:
    selected_function = input("\nYour choose: ")

    if selected_function.isnumeric():
        select = int(selected_function)
        break
    else:
        print(Fore.RED + "Error: You must enter a number! Enter again:\n" + Style.RESET_ALL)

if select == 1:
    result = sumarize(int1, int2)
elif selected_function == 2:
    result = substract(int1, int2)
elif selected_function == 3:
    result = multiply(int1, int2)
else:
    result = divide(int1, int2)

result = round(result, 3)
print(f"\nYour answer is: {result}\n")