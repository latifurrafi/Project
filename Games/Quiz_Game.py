# Quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Paris", "C) Madrid", "D) Rome"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) J.K. Rowling", "D) Mark Twain"],
        "answer": "B"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A) Oxygen", "B) Gold", "C) Hydrogen", "D) Carbon"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    }
]

def start_quiz():
    score = 0
    total_questions = len(quiz_data)

    print("Welcome to the Quiz Game!")
    print("Answer the following questions:\n")

    for i, q in enumerate(quiz_data):
        print(f"Question {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        # Get the player's answer
        answer = input("Your answer (A, B, C, or D): ").upper()
        
        # Check if the answer is correct
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    # Final score display
    print(f"You completed the quiz!")
    print(f"Your final score is: {score}/{total_questions}\n")

    # Show correct answers
    print("Here are the correct answers:")
    for i, q in enumerate(quiz_data):
        print(f"Question {i + 1}: {q['question']} - Correct answer: {q['answer']}")

# Start the quiz
if __name__ == "__main__":
    start_quiz()
