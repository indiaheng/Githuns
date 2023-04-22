from flask import Flask, request, render_template
from data import question_data
from questions import get_question, check_answer,  questions_left
from questions_api import get_q
import csv



app = Flask(__name__)
score = 0
questions_list = get_q()




@app.route('/')
def quiz():

    question = (get_question(questions_list))
    return render_template('quiz.html', question=question, score=score)

@app.route('/submit', methods=['POST'])
def submit():
    global score
    score, q_result = check_answer(request,score)
    if questions_left(questions_list) == True:
        question = (get_question(questions_list))

        return render_template('quiz.html', question=question, score=score, result=q_result)
    else:
        highest_score = 0
        with open("score.csv", mode="r", newline='') as data:
            writer = csv.reader(data)
            for row in writer:
                row_score = int(row[0])
                if row_score > highest_score:
                    highest_score = row_score
        if score > highest_score:
            with open("score.csv", mode="w", newline='') as data:
                writer = csv.writer(data)
                writer.writerow(f"{score}")
        return render_template("result.html", score=score)











if __name__ == "__main__":
     app.run(debug=True)