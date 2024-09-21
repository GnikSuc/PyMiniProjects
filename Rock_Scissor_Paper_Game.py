import random

class Game:
    def __init__(self, name):
        self.name = name
        self.selection = None
        self.chosen_item = None

    def make_selection(self):
        if self.name == "computer":
            self.selection = str(random.randint(1,3))
        else:
            self.selection = input("Enter your make_selection: ")
            while self.selection not in ["1","2","3"]:
                self.selection = input("Wrong selection. Enter valid make_selection: ")

        self.chosen_item = self.get_item(self.selection)
        return self.chosen_item

    def get_item(self, selection):
        mapping = {
            "1": "Rock",
            "2": "Scissor",
            "3": "Paper"
        }
        item = mapping.get(selection, "Unknown")
        print(f"{self.name} choice: {item}")
        return item

    def iswinner(self, computer_item):
        game_over = True

        if self.chosen_item == computer_item:
            print("It's a tie! Play again...")
            game_over = False

        # 1st option
        else: 
            if self.chosen_item == "Rock":
                if computer_item == "Scissor":
                    win = True
                else:
                    win = False
            if self.chosen_item == "Scissor":
                if computer_item == "Paper":
                    win = True
                else:
                    win = False
            if self.chosen_item == "Paper":
                if computer_item == "Rock":
                    win = True
                else:
                    win = False
        
        if not game_over == False:
            if win == True:
                print("You won!")
            elif win == False:
                print("Computer won!")

        return game_over



def main():
    print("Welcome to game Rock Scissor Paper!")
    while True:
        game_over = False

        player = Game("player")
        computer = Game("computer")

        while game_over == False:
            print("Choices:\n 1 - Rock\n 2 - Scissor\n 3 - Paper\n")
            player.make_selection()
            computer.make_selection()
            print()
            game_over = player.iswinner(computer.chosen_item)

        replay = input("Do you want to replay? (y/any): ").lower()
        if replay != "y":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()

