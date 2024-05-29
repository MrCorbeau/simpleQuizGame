from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def clear():
    return print(end="\033c")


question_bank = []
for q in question_data:
    text = q["text"]
    answer = q["answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():

    answer = quiz.next_question()
    correct_answer = question_bank[quiz.question_number - 1].answer
    quiz.check_answer(answer, correct_answer)

print(f"\n\nYou've completed the quiz and your final score is : {quiz.score}/{quiz.question_number}")
