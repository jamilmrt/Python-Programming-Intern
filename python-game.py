# This is a sample Python script.

# Quiz Game

# List of questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
        "answer": "c"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
        "answer": "b"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["a) Atlantic Ocean", "b) Indian Ocean", "c) Arctic Ocean", "d) Pacific Ocean"],
        "answer": "d"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["a) Charles Dickens", "b) William Shakespeare", "c) Mark Twain", "d) Jane Austen"],
        "answer": "b"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["a) 0", "b) 1", "c) 2", "d) 3"],
        "answer": "c"
    }
]


def ask_question(q):
    print(q["question"])
    for option in q["options"]:
        print(option)

    answer = input("Your answer (a, b, c, or d): ").lower()
    return answer == q["answer"]


def quiz():
    score = 0
    total_questions = len(questions)

    print("Welcome to the Quiz Game!")
    print(f"You will be asked {total_questions} questions.")

    for question in questions:
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was:", question["answer"], "\n")

    print(f"You scored {score} out of {total_questions}.")
    print("Thanks for playing!")


if __name__ == "__main__":
    quiz()

