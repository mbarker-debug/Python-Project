"""
Run the exam study game
"""

from User_Validation import get_hours
from study_functions import create_study_targets, study_event
from study_functions import sleep_cycle, check_game_status


def main():
    """
    Run the study game and let the player play again

    requests input and prints instructions and results
    """
    play_again = "yes"

    while play_again == "yes":
        print("\nWelcome to the exam study game!")
        print("You are preparing for three exams at Holy Cross.")
        print("You have 100 study hours to divide among the exams.")
        print("Each exam has a randomly chosen study target.")
        print("You must earn an A on all three exams to win.")
        print("Studying too little or too much can cost you an A.")
        print("You will receive a hint about one exam.")
        print("Your sleep choices determine your allowed difference.")
        print("You have three attempts to create a winning study plan.")

        total_study_hours = 100

        # Create the targets once so they stay the same for every attempt.
        target1, target2, target3 = create_study_targets(
            total_study_hours
        )

        study_event(target1, target2, target3)

        allowed_difference = sleep_cycle()

        print(
            "\nYour study hours can be",
            allowed_difference,
            "hour(s) above or below each target."
        )

        attempt = 1
        maximum_attempts = 3
        won = False

        while attempt <= maximum_attempts and won == False:
            print("\nAttempt", attempt, "of", maximum_attempts)
            print("Divide all 100 study hours among your three exams.")

            valid_hours = False

            while valid_hours == False:
                exam1_hours = get_hours(
                    "Hours for exam 1: ", 0, total_study_hours
                )
                exam2_hours = get_hours(
                    "Hours for exam 2: ", 0, total_study_hours
                )
                exam3_hours = get_hours(
                    "Hours for exam 3: ", 0, total_study_hours
                )

                hours_allocated = (
                    exam1_hours + exam2_hours + exam3_hours
                )

                if hours_allocated != total_study_hours:
                    print("Your study hours must add up to 100.")
                    print("You entered a total of", hours_allocated)
                    print("Please enter all three amounts again.")
                else:
                    valid_hours = True

            won = check_game_status(
                exam1_hours,
                exam2_hours,
                exam3_hours,
                target1,
                target2,
                target3,
                allowed_difference
            )

            if won == False and attempt < maximum_attempts:
                print("\nUse the feedback to adjust your study hours.")

            attempt = attempt + 1

        if won:
            print("\nYou win! You earned an A on all three exams!")
        else:
            print("\nYou lose. You used all three planning attempts.")

        print("\nThe actual study targets were:")
        print("Exam 1:", target1, "hours")
        print("Exam 2:", target2, "hours")
        print("Exam 3:", target3, "hours")

        play_again = input(
            "\nPlay again? Type yes or no: "
        ).strip().lower()

        while play_again != "yes" and play_again != "no":
            play_again = input(
                "Please type yes or no: "
            ).strip().lower()

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()