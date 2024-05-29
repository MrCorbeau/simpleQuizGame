class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        return input(f"Q {self.question_number} - {q.text} (True/False) : ").title()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
            print(f"The correct answer was : {correct_answer}")
        print(f"your current score is : {self.score}/{self.question_number}\n\n")


