"""
Study targets, random events, and exam results.
"""

import random

from User_Validation import get_hours


def create_study_targets(total_hours):
    """
    Return three positive integer targets that sum to total_hours.
    """
    exam1 = random.randint(1, total_hours - 2)
    remaining_hours = total_hours - exam1
    exam2 = random.randint(1, remaining_hours - 1)
    exam3 = remaining_hours - exam2
    return exam1, exam2, exam3

def study_event(exam1, exam2, exam3):
    """
    Reveals a study-hour range for one randomly selected exam.

    Inputs: three integer exam targets.
    """
    exam_selected = random.randint(1, 3)

    if exam_selected == 1:
        necessary_hours = exam1
    elif exam_selected == 2:
        necessary_hours = exam2
    else:
        necessary_hours = exam3
    
    
    minimum_hours = necessary_hours - random.randint(3,6)
    maximum_hours = necessary_hours + random.randint(3,6)

    # A study-hour hint should not include negative hours.
    if minimum_hours < 0:
        minimum_hours = 0

    print("\nYou attend a review session and receive a hint!")
    print(
        "Exam", exam_selected,
        "has a study target between",
        minimum_hours, "and", maximum_hours, "hours."
    )

def sleep_cycle():
    """
    Choose sleep for three nights and return the exam range.
    """

    rested_nights = 0
    total_sleep = 0
    print("\nPlan your sleep for the three nights before the exams.")
    print("Each night has a random game target from 6 to 9 hours.")
    print("Meeting at least two targets widens your study range to +/-2 hours.")
    print("Otherwise, your study range stays at +/-1 hour.")
    print("Sleep hours are separate from your 100 study hours.")

    for night in range(1, 4):
        print("\nNight", night)
        sleep_hours = get_hours("How many hours will you sleep? ", 0, 12)
        necessary_sleep = random.randint(6, 9)
        total_sleep = total_sleep + sleep_hours
        print("The sleep target for this night was", necessary_sleep)
        if sleep_hours == necessary_sleep + 1 or sleep_hours == necessary_sleep - 1 or sleep_hours == necessary_sleep:
            rested_nights = rested_nights + 1
            print("You met the sleep target!")
        else:
            print("You did not meet the sleep target.")

    print("\nTotal sleep:", total_sleep, "hours")
    print("Nights meeting the target:", rested_nights)
    if rested_nights >= 2:
        return 2
    else:
        return 1
    
def check_exam(study_hours, necessary_hours, allowed_difference):
    """
    Check whether allocated hours are within allowed_difference hours of the target.
    """
    minimum_hours = necessary_hours - allowed_difference
    maximum_hours = necessary_hours + allowed_difference
    if study_hours < minimum_hours:
        print("You understudied.")
        return False
    elif study_hours > maximum_hours:
        print("You overstudied.")
        return False
    else:
        print("You earned an A on this exam!")
        return True


def check_game_status(hours1, hours2, hours3, target1, target2, target3, allowed_difference):
    """
    Call check_exam for each exam and return whether all three earned As.
    """
    print("\nExam 1:")
    exam1_passed = check_exam(hours1, target1, allowed_difference)

    print("Exam 2:")
    exam2_passed = check_exam(hours2, target2, allowed_difference)

    print("Exam 3:")
    exam3_passed = check_exam(hours3, target3, allowed_difference)
    
    return exam1_passed and exam2_passed and exam3_passed
