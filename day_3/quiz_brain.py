class QuizBrain:
	def __init__(self, q_list):
		self.q_num = 0
		self.q_list = q_list
		self.score = 0

	def next_question(self):
		if self.check_finished():
			return False
		else:
			self.move_to_question()
			return True

	def move_to_question(self):
		def check_answer(answer):
			question = self.q_list[self.q_num]
			if answer.lower() == question.answer.lower():
				print("You got it right!")
				self.score+=1
			else:
				print(f"Wrong, sorry! \nThe correct answer was: {question.answer}")

		print(f"Your score is {self.score}/{self.q_num}\n")
		ans = input(f"Q.{self.q_num}: {self.q_list[self.q_num].text} (True/False) ")
		check_answer(ans)
		self.q_num+=1

	def check_finished(self):
		if self.q_num < len(self.q_list):
			return False
		else:
			print("\nYou finished the quiz!\n" \
					f"Your final score is {self.score}/{self.q_num}")
			return True