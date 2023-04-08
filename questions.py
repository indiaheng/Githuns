import random
from flask import request


def questions_left(questions_list):
    if len(questions_list) < 1:


        return False
    else:
        return True


def get_question(questions_list):
    question = (random.choice(questions_list))
    questions_list.remove(question)
    return question


#passing in score as shows the current score
def check_answer(request,score):
    user_answer = request.form['answer']
    correct_answer = request.form['correct_answer']
    q_result = "Incorrect"
    if user_answer == correct_answer:
        score += 1
        q_result = "Correct"
    return score, q_result







