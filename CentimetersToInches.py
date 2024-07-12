# Centimeters to inches convertor (without comment)

def centimeter_to_inches(value):
    result = round(value * 0.393700787, 2)
    unit = "inches"
    return result, unit

def inches_to_centimeters(value):
    result = round(value * 2.54, 2)
    unit = "centimeters"
    return result, unit

def chosen_function(choice, value):
    if choice == 1:
        result, unit = inches_to_centimeters(value)
    else:
        result, unit = centimeter_to_inches(value)

    return result, unit


def main():
    for i in range(0,64):
        print("=", end="")
    print(">")
    
    print("Welcome! This is centimeter/inch convertor...\n")
    choice = int(input("Select your conversion:\n[1.To centimeters]\n[2.To inches]\n> "))
    value = float(input("Enter value:\n> "))
    result, unit = chosen_function(choice, value)
    print(f"\nResult is {result} {unit}.")
    print("\nBye!\n")

if __name__ == "__main__":
    main()
