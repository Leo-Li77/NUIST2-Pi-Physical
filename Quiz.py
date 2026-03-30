# NUIST Quiz Game in Python

def quiz():
    print("Welcone to the Animal Quiz")
    print("Answer the following question:")

    # Questions and Answers
    questions = [
        "1. What is the largest animal on Earth? a. Blue Whale; b. Mouse; c. Cat\n",
        "2. Which bird can fly backwards? a. Cuckoo; b. Eagle; c. Hummingbird\n",
        "3. What is the only mammal capablr of flight? a. Bat; b. Squirrel; c. Dolphin\n"
    ]
    answers = [
        "a",
        "c",
        "a"
    ]
    score = 0

    # Ask questions
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            score += 1
            print("<Correct>")
        else:
            print("<Incorrect>")

    # Provide final score
    print("\n<Quiz Completed>")
    print(f"<You got {score}/{len(questions)} questions correct>")

# Run the quiz function
quiz()
