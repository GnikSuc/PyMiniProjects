import random
import math

number_of_game = 1
print("--------------------------------\nWelcome to guessing number game!\n")

while True:
    print(f"(Round {number_of_game})\n")

    while True:
        lower_number = int(input("Select lower bound: "))
        upper_number = int(input("Select upper bound: "))

        if upper_number <= lower_number or abs(upper_number - lower_number) == 1:
            print("Error: You entered numbers wrong! Enter again...\n")
        else:
            break

    random_number = random.randint(lower_number, upper_number)

    tries = round(math.log(upper_number - lower_number + 1, 2))
    print(f"\nYou have {tries} tries to guess the right number:\n")

    counter = 0

    while counter < tries:
        guess = int(input("Enter your guess: "))
        counter = counter + 1

        if guess == random_number:
            print("Congratulations! You guessed it right.\n")
            status = 1
            break
        elif guess < random_number:
            print(f"Too low!\tThe remaining tries: {tries - counter}\n")
        else:
            print(f"Too high!\tThe remaining tries: {tries - counter}\n")
        
        
    if counter == tries or status != 1:
        print("Sorry, you are out of tries")
        
    repeat = input("Would you like to play again?(y/anything else): ")
    
    if repeat == "Y" or repeat == "y":
        number_of_game = number_of_game + 1
        print("")

    else:
        print("--------------------------------")
        break
