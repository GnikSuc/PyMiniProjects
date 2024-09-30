import random as rn
import time

days_in_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

def game(correct, all_tips):
    random_month = rn.choice(list(days_in_month.keys()))
    days = str(days_in_month[random_month])
    question = str(input(f"How many days does {random_month} have?\n"))
    if question == days:
        print("True!")
        correct += 1
        all_tips += 1
        
    else:
        print(f"False. The right number was {days}.")
        all_tips += 1
    return correct, all_tips

def success_rate(correct_tips, all_tips):
    return f"{(correct_tips / all_tips * 100):.2f} % | correct: {correct_tips} | all: {all_tips}\n"

def main():

    print("\nHello player, let's start!\n")
    correct_tips = 0
    all_tips = 0
    while True:
        correct_tips, all_tips = game(correct_tips, all_tips)
        print(success_rate(correct_tips, all_tips))
        time.sleep(2)

if __name__ == "__main__":
    main()


