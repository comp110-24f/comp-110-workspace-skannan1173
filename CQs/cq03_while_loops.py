"""My third challenge question in COMP110! - while loops"""

__author__ = "730536653"


def num_instances(phrase: str, search_char: str) -> int:
    """This function takes a phrase and returns the number of search char"""
    count: int = 0  # Local variable to start counting at 0
    index: int = 0  # Local varibable to start index at 0
    while index < len(phrase) - 1:
        # While loop runs for every index of the phrase starting at 0 to len(phrase) - 1
        if phrase[index] == search_char:
            # Runs if the indexed letter equals search char
            count += 1
            # Increases count by 1 if the specified index equals the search char
        index += 1
        # Increases the index by 1 for every loop to index consequtively
    return count
    # Once the index surpasses the len(phrase) - 1,  the index will return an error
    # While loop will stop running
    # Final count of the search char is returned
