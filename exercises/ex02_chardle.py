"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730536653"


def input_word() -> str:
    # Prompts the user to input their 5-character word guess
    guess_word = input("Enter a 5-character word: ")
    # Checks if length of the input guess word is 5 characters
    if len(guess_word) != 5:
        # Prints error message if length of input guess word is not equal to 5
        print("Error: Word must contain 5 characters.")
        # Exits program if the guess word input length is not equal to 5
        exit()
    return guess_word


def input_letter() -> str:
    # Prompts the user to input their 1-character letter guess
    letter = input("Enter a single character: ")

    # Checks if length of the input letter is equal to 1 character
    if len(letter) != 1:
        # Prints an error message if the length of the input  letter is not equal to 1
        print("Error: Character must be a single character.")
        # Exits the program if the letter input length is not equal to 1
        exit()
    return letter


def contains_char(guess_word: str, letter: str) -> None:
    # Tests each index of the guess word to see if there is a match with the letter
    # If an index doesn't match, continues to the next if block
    # We don't need an output for every if statement, only need to outpring the matches
    # Count stores the number of indexes in the guess word that match the letter
    # Count starts at 0 and increments by 1 only if index equals letter
    count: int = 0
    print("Searching for " + str(letter) + " in " + str(guess_word))
    if guess_word[0] == letter:
        print(str(letter) + " found at index 0")
        count += 1
    if guess_word[1] == letter:
        print(str(letter) + " found at index 1")
        count += 1
    if guess_word[2] == letter:
        print(str(letter) + " found at index 2")
        count += 1
    if guess_word[3] == letter:
        print(str(letter) + " found at index 3")
        count += 1
    if guess_word[4] == letter:
        print(str(letter) + " found at index 4")
        count += 1

    # Prints the output of letter count based on final value of count
    if count == 0:
        print("No instances of " + str(letter) + " found in " + str(guess_word))
    elif count == 1:
        print("1 instance of " + str(letter) + " found in " + str(guess_word))
    else:
        print(
            str(count) + " instances of " + str(letter) + " found in " + str(guess_word)
        )


# Combines input_word and input_letter functions and call them together
def main() -> None:
    contains_char(guess_word=input_word(), letter=input_letter())


# Allows program to run
if __name__ == "__main__":
    main()
