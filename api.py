from html import unescape
import requests
import random

# Fetch questions from Open Trivia DB API
def fetch_questions():
    while True:
        url = "https://opentdb.com/api.php?amount=10&type=multiple"
        response = requests.get(url)
        if response.ok:
            question_data = response.json()
            return question_data["results"]
        print("Retrying...")

# Quiz logic
def question_generator(score,questions):
    question_counter = 1

    for a_question in questions:
        print(f"\nQuestion {question_counter}: {unescape(a_question['question'])}\n")
        question_counter += 1

        answers = a_question["incorrect_answers"] + [a_question["correct_answer"]]
        random.shuffle(answers)

        for answer in answers:
            print(f"\t{unescape(answer)}")

        while True:
            user_answer = input("\nPlease type the correct answer: ").strip().upper()
            correct = a_question["correct_answer"].strip().upper()

            if user_answer == correct:
                print("\nCorrect!")
                score += 1
                break
            elif user_answer[:20:2] == correct[:20:2]:
                print("\nClose enough!")
                score += 1
                break
            else:
                print("\nIncorrect")
                break

    print(f"\nYou answered {score} out of {len(questions)} correctly")
    with open("quiz_results.txt", "a") as file:
        file.write(f"You answered {score} out of {len(questions)} questions correctly.\n")

#run quiz
print("Welcome to my Quiz!")
username = input("What is your name? ")
with open("quiz_results.txt", "a") as file:
    file.write(f"{username}.\n")
score = 0
question_generator(score, fetch_questions())