import random


def questions_left(questions):
    if len(questions) < 1:
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
    if user_answer == correct_answer:
        score += 1
    return score