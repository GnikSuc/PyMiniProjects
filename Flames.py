def input_names():
    name1 = input("Enter first name: ").upper()
    name2 = input("Enter second name: ").upper()
    logic(name1, name2)
    return

def logic(n1, n2):
    relationship_list = ['Friends', 'Lovers', 'Affection', 'Marriage', 'Enemies', 'Siblings']
    common_letters = []
    remaining_letters = []
    for i in n1:
        if i in n2 and not i in common_letters:
            common_letters += i
        elif i in remaining_letters or i in common_letters:
            continue
        else:
            remaining_letters += i
    for i in n2:
        if i not in remaining_letters and i not in common_letters:
            remaining_letters += i

    common_letters_str = ', '.join(common_letters)
    remaining_letters_str = ', '.join(remaining_letters)
    number_of_letters = (len("".join(remaining_letters)) -1) % len("FLAMES")
    relationship = relationship_list[number_of_letters]

    print(f"\nCommon letters are: {common_letters_str}")
    print(f"There are {number_of_letters} letters after removing common ones: {remaining_letters_str}")
    print(f"Word {relationship[0]} is on position ({number_of_letters}) and it stands for ''{relationship}''.\n")
    return


def main():
    print("\nWelcome to FLAMES!")
    print("The word 'FLAMES' stands for different types of relationships:\nFriends, Lovers, Affection, Marriage, Enemies and Siblings.")
    input_names()
    print("Bye!")


if __name__ == "__main__":
    main()