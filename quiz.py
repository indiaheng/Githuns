from flask import Flask, request, render_template
import random
from data import question_data




app = Flask(__name__)
score = 0
questions = question_data


def get_question():
    if len(questions) < 1:
        return "Game Complete"
    else:
        question = (random.choice(questions))
        questions.remove(question)
        return question








@app.route('/')
def quiz():

    question = (get_question())
    return render_template('quiz.html', question=question, score=score)

@app.route('/submit', methods=['POST'])
def submit():
    question = (get_question())
    user_answer = request.form['answer']
    correct_answer = request.form['correct_answer']
    if user_answer == correct_answer:
        global score
        score += 1

        return render_template('quiz.html', question=question, score=score)
    else:
        return render_template('quiz.html', question=question, score=score)



if __name__ == "__main__":
     app.run(debug=True)