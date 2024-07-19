import random
import time


def set_random_number():
    num = random.randint(1000, 10000)
    return str(num)

def player_guess():
    num = set_random_number()
    #num = str(1111)
    attempt = 1
    while True:
        guess = input(("Enter your guess: "))
        if not guess.isnumeric or range(1000, 10000):
            pass
        
        guess = str(guess)
        i = 0
        for _ in num:
            if guess[i] == _:
                print(_, end=" ")
            else:
                print("X", end=" ")
            i += 1

        if guess == num:
            print(f"Congratulation! You guessed it in {attempt} attempt{'s' if attempt != 1 else ''}.")
            break
        else:
            attempt += 1
    return attempt

def computer_guess():
    while True:
        num = input("Enter four-digit number: ")
        if num.isnumeric and range(1000, 10000):
            break
    time.sleep(0.5)

    guess = "0000"
    new_guess = guess
    attempt = 1
    while True:
        time.sleep(0.5)
        num = str(num)
        i = 0
        for _ in guess:
            if num[i] == _:
                rewriting = False
                print(_, end=" ")
            else:
                rewriting = True
                print("X", end=" ")
            new_guess = rewrite_guess(_, i, new_guess, rewriting)
            i += 1

        if guess == num:
            print(f"Computer guessed it in {attempt} attempt{'s' if attempt != 1 else ''}.")
            break
        else:
            attempt += 1
        print(end="\n")
        guess = new_guess
    return attempt

def rewrite_guess(char, i, new_guess, rewriting):
    if rewriting == False:
        pass
    else:
        char = str(int(char) + 1)
    char_list = list(new_guess)
    char_list[i] = char
    new_guess = ''.join(char_list)
    return new_guess


def game():
    print("Welcome to Mastermind!")
    print("(Your turn)")
    player = player_guess()
    print("(Computer turn)")
    computer = computer_guess()
    print(f"Attempts: [Human: {player} |Computer: {computer} ]")
    if player < computer:
        print("Congratulation! You won.")
    elif player == computer:
        print("It's a tie!")
    else:
        print("You lost! Maybe next time...")


def main():
    game()

if __name__ == "__main__":
    main()
