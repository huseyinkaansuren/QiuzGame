from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
category = input("Please select category(History/Computer/Film):").lower()
difficulty = input("Please select difficulty(easy/medium/hard:").lower()
for question in question_data:
    if category in question["category"].lower() and difficulty in question["difficulty"].lower():
        new_q = Question(question["question"],question["correct_answer"])
        question_bank.append(new_q)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_number}")