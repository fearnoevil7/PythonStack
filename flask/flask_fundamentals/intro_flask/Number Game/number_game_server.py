from flask import Flask, render_template, request, redirect, session,flash , url_for
import random
app = Flask(__name__)
app.secret_key='my_little_secret'

@app.route('/')
def index():
    if 'message' not in session:
        session['message'] = ''
    if 'num' not in session:
        session['num'] = random.randrange(1, 101)
    return render_template("number_game.html", message = session['message'])

@app.route('/guess', methods = ['POST'])
def too_high():
    guess= int(request.form['number'])
    if guess > session['num']:
        session['message']= "Too High"
    if guess < session['num']:
        session['message']= "Too Low"
    elif guess == session['num']:
        session['message']= "You Win!!!!!!!"
    return redirect('/')

@app.route('/reset')
def reset():
    session['num']
    session.pop("num")
    session.pop("message")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)