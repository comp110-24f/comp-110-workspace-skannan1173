"""This program will be used to calculate the logistics of a tea party"""

__author__: str = "730536653"


# Convert guests, tea_bags, and treats to strings
# Concatenate with the rest of the str output
# Keyword argument for tea_bags and treats is people = guests
# The input for main_planner is guests and this goes into the input for the subfunctions
# tea_count and treat_count are obtained by calling to the tea_bags and treats functions
def main_planner(guests: int) -> None:
    """Outputs the number of tea bags, treats, and total cost for the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


# Assume each guest drinks 2 cups of tea -> people times 2
def tea_bags(people: int) -> int:
    """Calculates the number of tea bags given the number of people"""
    return people * 2


# Assume each guest has 1.5 treats per cup of tea
# Call to function tea_bags to get the number of cups of tea
# Multiply cups of tea by 1.5 to get number of treats
def treats(people: int) -> int:
    """Calculates the number of treats given the number of teas each person drinks"""
    return int(tea_bags(people=people) * 1.5)


# Each tea bag costs $0.50 and each treat costs $0.75
# Multiply tea_count and treat_count with its respective price
# Sum both prices of both tea_count and treat_count to get total cost
def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost given the number of tea bags and treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


# Makes program runnable
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
