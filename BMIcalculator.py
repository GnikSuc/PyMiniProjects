# BMI in metric system (without comment)


def enter_values():
    Weight = float(input("Please enter your weight in kilograms:\n"))
    Height = float(input("Please enter your height in centimeters:\n"))

    #while not Weight: float and Height: float:
    return Weight, Height

def Calculate_BMI(Weight, Height):
    BMI = round(Weight / ((Height/100) ** 2), 1)
    return BMI

def define_physique(BMI):
    if BMI < 18.5:
        condition = ("underweight")
    elif 18.5 <= BMI < 25:
        condition = ("in normal condition")
    elif 25 <= BMI < 40:
        condition = ("overweight")
    elif BMI >= 40:
        condition = ("obese")

    return condition


def main():
    print("Welcome to BMI calculator in metric system.\n")
    Weight, Height = enter_values()
    BMI = Calculate_BMI(Weight, Height)
    print(f"Your BMI is {str(BMI)}.\nYou are {Calculate_BMI(BMI)}.")
    print("\nBye!\n")

if __name__ == "__main__":
    main()
