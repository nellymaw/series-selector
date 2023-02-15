import random


def add_series(user_input):
    """
    Allows the user to add a series to the list.
    """
    with open('series.txt', 'w') as file:
        file.writelines(user_input)


def visualize_series():
    with open('series.txt', 'r') as file:
        series = file.readlines()
    return series


def random_series():
    """
    Randomly selects a series from the list.
    """
    return random.choice(visualize_series())
