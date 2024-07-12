import random
import math


def underscore():
    for i in range(0, 56):
        print("_", end="")

def enter_values():
    while True:
        low_num = int(input("> Select lower bound: "))
        upp_num = int(input("> Select upper bound: "))
        if upp_num <= low_num or abs(upp_num - low_num) == 1:
            print("Error: You entered numbers wrong! Enter again...\n")
        else:
            return low_num, upp_num
        
def set_random_num(low_num, upp_num):
    random_num = random.randint(low_num, upp_num)
    return random_num

def set_attemps(low_num, upp_num):
    attemps = round(math.log(upp_num - low_num + 1, 2))
    print(f"\n (You have {attemps} attemps to guess the right number)\n\n")
    return attemps

def game(random_num, attemps, won, lost):
    counter = 0
    won_so_far = won
    while counter != attemps:
        guess = int(input("> Enter your guess: "))
        counter += 1
        if guess == random_num:
            print(f" Congratulations! You guessed it right on attempt nr. {counter}.\n")
            won += 1
            break
        elif guess < random_num:
            print(f" Too low!\t\t The remaining attemps: {attemps - counter}\n")
        else:
            print(f" Too high!\t\t The remaining attemps: {attemps - counter}\n")
    if counter == attemps and won == won_so_far:
        print(" Sorry, you are out of attemps. :(")
        lost += 1
    return won, lost

def end(game_num, won, lost):
    Q = input("> Repeat? (Y/press any other key): ")
    Q = Q.upper()
    if Q == "Y":
        repeat = True
        game_num += 1
    else:
        repeat = False
        print(f"\n\n (Game over | You {won}:{lost} Computer | rounds: {game_num} )")
        underscore()
    return game_num, repeat
        

def main():
    underscore()
    print("\n\n\t--- Welcome to number guessing game! ---\n")
    game_num = 1
    won = 0
    lost = 0
    while True:
        underscore()
        print(f"\n ( You {won}:{lost} Computer | Round: {game_num} )\n")
        low_num, upp_num = enter_values()
        random_num = set_random_num(low_num, upp_num)
        attemps = set_attemps(low_num, upp_num)
        won, lost = game(random_num, attemps, won, lost)
        game_num, repeat = end(game_num, won, lost)
        if repeat == False:
            break

if __name__ == "__main__":
    main()
