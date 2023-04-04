import random
from quiz import questions

class Question_quiz:


    def get_question(self):
        if len(questions) < 1:
            return "Game Complete"
        else:
            question = (random.choice(questions))
            questions.remove(question)
            return question

