from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(single_q["text"],single_q["answer"]) for single_q in question_data]

brain  = QuizBrain(question_bank)
while brain.next_question():
	pass
