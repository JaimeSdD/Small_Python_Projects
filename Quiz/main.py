from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bag = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bag.append(new_question)

quiz = QuizBrain(question_bag)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")