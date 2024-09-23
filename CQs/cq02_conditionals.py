"""My second challenge question in COMP110!"""

__author__ = "730536653"


def guess_a_number() -> None:
    """Takes a numerical input from the user and compares it to secret number"""
    # Secret number given
    secret = 7
    # Asks user to input their numerical guess
    guess = int(input("Guess a number: "))
    # Prints the number inputted by the user to confirm their guess
    print("Your guess was " + str(guess))

    # Evaluates the inpuet guessed by the user
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
