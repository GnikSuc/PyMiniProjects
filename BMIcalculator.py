# BMI in metric system (without comment)

print("Welcome to BMI calculator in metric system.")

Weight = float(input("Please enter your weight in kilograms:\n"))
Height = float(input("Please enter your height in centimeters:\n"))
print("")

BMI = round(Weight / ((Height/100) ** 2), 1)

if BMI < 18.5:
    condition = ("underweight")
elif 18.5 <= BMI < 25:
    condition = ("in normal condition")
elif 25 <= BMI < 40:
    condition = ("overweight")
elif BMI >= 40:
    condition = ("obese")


print("Your BMI is " + str(BMI) + "...\nYou are " + condition + ".\n")
