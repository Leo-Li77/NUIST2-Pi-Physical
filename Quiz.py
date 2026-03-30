# NUIST Quiz Game in Python
# Author: Leo Li
# Date:   2026/3/30

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Red light
GPIO.setup(18, GPIO.OUT)
# Green light
GPIO.setup(17, GPIO.OUT)

def quiz():
    print("Welcone to the Animal Quiz")
    print("Answer the following question:")

    # Questions and Answers
    questions = [
        "1)What is the largest animal on Earth?\na)Blue Whale\nb)Mouse\nc)Cat\n",
        "2)Which bird can fly backwards?\na)Cuckoo\nb)Eagle\nc)Hummingbird\n",
        "3)What is the only mammal capable og flight?\na)Bat\nb)Squirrel\nc)Dolphin\n"
    ]
    answers = [
        "a",
        "c",
        "a",
    ]
    score = 0

    # Ask questions
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            score += 1
            print("<Correct>")
            GPIO.output(17, GPIO.HIGH)
            print("<The green LED is lighting>")
            time.sleep(2)
            GPIO.output(17, GPIO.LOW)
        else:
            GPIO.output(18, GPIO.HIGH)
            print("<Incorrect>")
            print("<The red light is lighting>")
            time.sleep(2)
            GPIO.output(18, GPIO.LOW)
    # Provide final score
    print("\n<Quiz Completed>")
    print(f"<You got {score}/{len(questions)} questions correct>")

# Run the quiz function
quiz()
