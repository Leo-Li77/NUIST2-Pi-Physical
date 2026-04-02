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
    print("Welcone to the Python Code Quiz")
    print("Answer the following questions:")

    # Questions and Answers
    questions = [
        "1)Which of the following is NOT a python data type?\na)int\nb)float\nc)rational\nd)string\ne)bool\n",
        "2)Which of the following is NOT a built-in operation in Python?\na)+\nb)%\nc)abs()\nd)sqrt()\n",
        "3)In a mixed-type expression involving ints and floats, Pyhton will convert:\na)floats to ints\nb)ints to strings\nc)floats and ints to strings\nd)ints to floats\n",
        "4)The best structure for implementing a multi-way decision in Python is:\na)if\nb)if-else\nc)if-elif-else\nd)try\n",
        "5)What statement can be executed in the body of a loop to cause it to terminate?\na)if\nb)exit\nc)continue\nd)break\n"
    ]
    answers = [
        "c",
        "d",
        "d",
        "c",
        "d"
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
