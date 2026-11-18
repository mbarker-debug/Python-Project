"""
Functions for reading the player's answers
"""


def get_hours(prompt, minimum, maximum):
    """
    Ask for a whole number within the allowed limits.

    Inputs: a prompt and minimum and maximum integers.
    Output: a valid integer.
    Side effects: requests input and prints error messages.
    """
    while True:
        try:
            hours = int(input(prompt))

            if hours < minimum or hours > maximum:
                print("Enter a number from", minimum, "to", maximum)
            else:
                return hours

        except ValueError:
            print("Please enter a whole number.")


def ask_play_again():
    """
    Ask for replay input and return 'yes' or 'no' for end of code
    """
    answer = input("Play again? Type yes or no: ").strip().lower()
    while answer != "yes" and answer != "no":
        answer = input("Please type yes or no: ").strip().lower()
    return answer