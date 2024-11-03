# This is e creating a Basic Quiz Game using the Python programming language.
# from typing import Dict

quiz_questions: dict[
    str, dict[str, dict[str, str] | str] | dict[str, dict[str, str] | str] | dict[str, dict[str, str] | str] | dict[
        str, dict[str, str] | str]] = {
    "What is the capital of France?": {
        "options": {
            "A": "Berlin",
            "B": "Paris",
            "C": "London",
            "D": "Rome"
        },
        "Answer": "B"
    },
    "Which planet is known as the Red Planet?": {
        "options": {
            "A": "Earth",
            "B": "Mars",
            "C": "Jupiter",
            "D": "Saturn"
        },
        "Answer": "B"
    },
    "Who painted the famous painting 'The Starry Night'?": {
        "options": {
            "A": "Leonardo da Vinci",
            "B": "Vincent van Gogh",
            "C": "Pablo Picasso",
            "D": "Claude Monet"
        },
        "Answer": "B"
    },
    "What is 2 + 2?": {
        "options": {
            "A": "3",
            "B": "4",
            "C": "5",
            "D": "6",
        },
        "Answer": "B"
    },

}


def display_question(question, options):
    """Display the question and options to the user."""
    print(question)
    for option, value in options.items():
        print(f"{option}: {value}")


def get_user_answer():
    """Get the user's answer and validate it."""
    while True:
        answer = input("Choose your answer (A, B, C, D): ").upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        else:
            print("Invalid input. Please choose A, B, C, or D.")


def quiz_game():
    score = 0
    total_questions = len(quiz_questions)

    for question, details in quiz_questions.items():
        display_question(question, details["options"])
        answer = get_user_answer()

        if answer == details["Answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer is {details['Answer']}.\n")

    print(f"Your final score is {score} out of {total_questions}.")


# Run the quiz game
quiz_game()
