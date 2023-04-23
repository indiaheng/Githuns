from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder='templates')

@app.route('/')
def leaderboard():
  # #  conn = sqlite3.connect('database.db')
  #  # c = conn.cursor()
  #   c.execute('SELECT name, score FROM leaderboard ORDER BY score DESC')
  #   data = c.fetchall()
  #   conn.close()
    return render_template('leaderboard.html')

if __name__ == '__main__':
    app.run(debug=True)
