from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for n in question_data:
    question = n["text"]
    question_answer = n["answer"]
    ques = Question(question, question_answer)
    question_bank.append(ques)

qb = QuizBrain(question_bank)

while qb.still_have_question():
    qb.nex_question()
