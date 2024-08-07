from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
n = len(question_data)
for i in range(n):
    question_bank.append(Question(question_data[i]["question"], question_data[i]["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you've completed the quiz!")
print(f"your final score is {quiz.score}/{quiz.question_number}")
