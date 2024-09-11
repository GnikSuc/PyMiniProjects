#Morse coder/deco
import re


def selection(alphabet_chars, morse_chars):
    while True:
        select = input("Please select by typing number only: ")
        user_input = input("Please enter input: ")
        if select == "1":
            output = coder(user_input, alphabet_chars, morse_chars)
            break
        elif select == "2":
            output = decoder(user_input, alphabet_chars, morse_chars)
            break
        else:
            print("Invalid input! Please enter again...")
    
    print(f"\nOutput: {output}")
    print("Would you like to Continue? (y/n) ", end="")

def coder(user_input, alphabet_chars, morse_chars):
    output = ""
    unwanted = ["/", ",", ".", "-", " "]
    separ = separator()

    for char in user_input.lower():
        if char not in unwanted:
            num_char = alphabet_chars.index(char)
            output += morse_chars[num_char] + separ
    return output

def decoder(user_input, alphabet_chars, morse_chars):
    output = ""
    separ = separator()
    user_input = user_input.split(separ)
    user_input = [item for item in user_input if item != ""]

    for char in user_input:
        num_char = morse_chars.index(char)
        output += alphabet_chars[num_char]
    return output

def separator():
    separator = input("Please enter separator: ")
    if separator == "":
        separator = " "
    return separator

def main():
    alphabet_chars = "abcdefghijklmnopqrstuvwxyz"
    morse_chars = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
    "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
    "...-", ".--", "-..-", "-.--", "--.."]
    print("\nWelcome to Morse coder/decoder!\n")
    end = False

    while end == False:
        print("[ (1). Coder (insert text) ]")
        print("[ (2). Decoder (insert code) ]")
        print("[ Default separator: space ]\n")
        selection(alphabet_chars, morse_chars)
        while True:
            answer = input().lower()
            if answer == "y":
                break
            elif answer == "n":
                print("\nOK, bye!\n")
                end = True
                break
            else:
                print("Sorry, I don't understand. Type Again: ", end="")

if __name__ == "__main__":
    main()

