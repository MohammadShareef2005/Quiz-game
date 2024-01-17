class QuizBrain:
    def __init__(self, a):
        self.question_number = 0
        self.question_list = a
        self.score = 0

    def still_have_question(self):
        if self.question_number < (len(self.question_list)):
            return True
        else:
            return False

    def nex_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        b = input(f"Q.{self.question_number }: {current_question.text} (True/False)?:").lower()
        self.check_answer(b, current_question)

    def check_answer(self, u_answer, ans):
        if ans.answer.lower() == u_answer:
            self.score += 1
            print("you got it right!")

        else:
            print("That's wrong")
        print(f"the correct answer was: {ans.answer}")
        print(f"your current score is {self.score}/{self.question_number}.")
