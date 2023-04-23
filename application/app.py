from flask import Flask, render_template, request
import pymysql.cursors
from sqlalchemy import true

app = Flask(__name__)

connection = pymysql.connect(host="localhost",
                         port=3306,
                         user="root",
                         password="password",
                         database="githuns",
                         charset="utf8mb4",
                         cursorclass=pymysql.cursors.DictCursor)


categories = ["General Knowledge", "Music", "History", "Movies", "Science"]
currentUser = ''

# https://neil.tesaluna.com/posts/connecting-flask-to-aws-rds/

@app.route("/")
def home():
    return "<h1>Home Page</h1>"


@app.route("/menu", methods=['GET', 'POST'])
def menu():
    if request.method == 'POST' and 'name' in request.form:
        # fetch the form data - the user's name
        username = request.form['name']

        connection.ping(reconnect=True)

        # save name to the db
        with connection:
            with connection.cursor() as cursor:
                #         Insert form data into database
                sql = "INSERT INTO scores(name) VALUES (%s)"
                cursor.execute(sql, username)
        #     commit connection to save changes to the database
            connection.commit()
            print(f'username: {username} has been saved into db')

    return render_template('menu.html', categories=categories)


@app.route("/start/<category>")
def start(category):
    #     select name from db

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT name FROM scores ORDER BY ID DESC LIMIT 1"
            cursor.execute(sql)
            result = cursor.fetchone()
            currentUser = result

    return render_template('start.html', category=category, name=currentUser)



# run the app in debug mode
# so app reloads when changes have been made
if __name__ == "__main__":
    # dbconnect()
    app.run(debug=True)

