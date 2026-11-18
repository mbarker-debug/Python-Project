import random

def check_exam(study_hours, necessary_hours):
    """Check whether study hours fall within the A grade range"""

    minimum_hours = necessary_hours - 1
    maximum_hours = necessary_hours + 1

    print ("The acceptable range was ", minimum_hours, " to", maximum_hours)

    if study_hours < minimum_hours:
        print("You understudied.")
        return False

    elif study_hours > maximum_hours:
        print("You overstudied.")
        return False
    
    else:
        print("You earned an A on this exam")
        return True
    

def main():
    """Run the study game and allow user to choose if they want to play again."""

    play_again = "yes"

    while play_again == "yes":
        print("You have three exams and four days to study.")
        print("You must get your study hours for eaxch exam in the random range required")

        # Asking for the total hours they want to study
        total_study_hours = int(input("Choose total study hours from 3 to 96 hours: "))
        
        while total_study_hours < 3 or total_study_hours > 96:
            total_study_hours = int(input("Choose total study hours from 3 to 96 hours: "))

        # randomly divide the total into study target for the 3 exams
        exam1_necessary = random.randint(1, total_study_hours - 2)
        remaining_hours = total_study_hours - exam1_necessary
        exam2_necessary = random.randint(1, remaining_hours - 1)
        exam3_necessary = remaining_hours - exam2_necessary

        # Ask how the player wants to split their hours between exams
        valid_hours = False

        while valid_hours == False:
            exam1_hours = int(input("Hours for exam 1: "))
            exam2_hours = int(input("Hours for exam 2: "))
            exam3_hours = int(input("Hours for exam 3: "))

            hours_allocated = exam1_hours + exam2_hours + exam3_hours

            if exam1_hours < 0 or exam2_hours < 0 or exam3_hours < 0:
                print("Study hours cannot be negative.")
            elif hours_allocated != total_study_hours:
                print("Your hours must add up to", total_study_hours)
            else:
                valid_hours = True

        # use function above to check each exam
        print("Exam 1: ")
        exam1_passed = check_exam(exam1_hours, exam1_necessary)

        print("Exam 2: ")
        exam2_passed = check_exam(exam2_hours, exam2_necessary)

        print("Exam 3: ")
        exam3_passed = check_exam(exam3_hours, exam3_necessary)

        # player must pass all three exams to win or get an A
        if exam1_passed and exam2_passed and exam3_passed:
            print("You win! You earned an A on all three exams!")
        
        else: 
            print("You lose. Try again!")
        
        play_again = input("Play again? Type yes or no: ").lower()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()






