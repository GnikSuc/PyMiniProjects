#Hangman
import random

#from .txt to list
def Convert(string): 
    li = list(string.split("\n"))
    return li

file = open("job_list.txt", "r")
content = file.read()
file.close()
list_of_words = Convert(content)

word = random.choice(list_of_words)
guessed_letters = ""
#word = "bla bla"
chance = len(word) + 2
num_try = 0
gap = 0

for i in range(8):
    print("-_-_", end="")
print("\nWelcome to hangman game!")
print(f"Guess the job, you have {chance} tries.\n")

for x in word:
    if x != " ":
        print("_", end="")
    else:
        print(" ", end="")
        gap += 1

print("")
chance = chance - gap

while num_try != chance:
    num_try += 1

    while True:
        guess = input("\nEnter a letter: ")
        
        if len(guess) > 1:
            print("Enter only one letter!")
        else:
            break

    if guess in word:
        y = word.count(guess)
        for letter in range(y):
            guessed_letters += guess

    for letter in word:
        if letter in guessed_letters:
            print(letter, end="")
        elif letter == " ":
            print(" ", end="")
        else:
            print("_", end="")

    if len(guessed_letters) == (len(word) - gap):
        print("\n\nCongratulations! You guessed the word right!")
        print("\nBye!\n")
        break
    elif num_try == chance:
        print("\n\nMaybe next time...")
        print("\nBye!\n")
