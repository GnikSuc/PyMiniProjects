#Guessing game 2#
import random
import math

print("\nHello gamer!\nWelcome to guessing game focused on fruit!\n")

fruits = ["Banana","Watermelon","Mango","Orange","Strawberry","Avocado","Blueberry","Blackberry","Kiwi","Cherry","Guava","Peach","Plum","tomato","Apricot"]
number_of_fruits = 0
print(fruits)

for fruit in fruits:
    number_of_fruits = number_of_fruits + 1

tries = round(math.sqrt(number_of_fruits), 0)
tries_string = str(tries)

print(f"There are {number_of_fruits} Fruits. You have {tries_string[0]} tries.\n")

counter = 1
random_word = random.choice(fruits)
#print(f"test: {random_word}")

while counter < tries + 1:
    print(f"\nTry nr. {counter}")
    answer = input("Your answer: ")
    
    if answer == random_word:
        print("\nCongratulation! You passed!\n")
        break
    elif counter == tries:
        print(f"\nUps, you didn't make it. The guessed fruit was {random_word}\nMaybe next time...\n")
        counter = counter + 1
    else:
        counter = counter + 1