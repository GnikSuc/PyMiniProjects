#Guessing game 2#
import random
import math

def get_content_data():
    with open("fruit_list.txt", "r") as file:
        content = file.read()
    fruits = list(content.split("\n"))

    fruit_num = 0
    for fruit in fruits:
        fruit_num += 1

    return fruits, fruit_num

def attempts(fruit_num):
    tries = int(math.ceil(fruit_num/3))
    print(f"There are {fruit_num} Fruits. You have {tries} attempts. Probability is {round((tries/fruit_num)*100, 2)}%. :)\n")
    return tries

def game(tries, fruits):
    counter = 1
    random_word = random.choice(fruits)

    while counter < tries + 1:
        print(f"Try nr. {counter}")
        answer = input("Your answer: ")
        
        if answer == random_word:
            print("\nCongratulation! You passed!\n")
            break
        elif counter == tries:
            print(f"\nUps, you didn't make it. :( The guessed fruit was {random_word}.\n\nMaybe next time...")
            counter += 1
        else:
            answers = ["Unfortunately not that word...", "No, that isn't it.", "Try again."]
            counter += 1
            print(random.choice(answers) + f"You still have {tries - counter + 1} attempts. :)")

def underscore():
    for i in range(0, 48):
        print("_", end="")

def main():
    underscore()
    print("\nWelcome to guessing game focused on fruit, gamer!\n")
    fruits, fruit_num = get_content_data()
    print(f"Here are fruits contained in list:\n{fruits}\n")
    tries = attempts(fruit_num)
    game(tries, fruits)
    underscore()


if __name__ == "__main__":
    main()