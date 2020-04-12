from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key='this_is_secret'

@app.route('/')
def index():
    if 'userGold' not in session:
        session['userGold'] = 0
    
    return render_template("ninja_oro.html", total = session['userGold'])

@app.route('/activities', methods = ['POST'])
def ninja_activities():
    # print(request.form) 
    # remember to print request form to check the immutable dictionary for help and then check the console
    # print(request.form['building'])
    if request.form.get('building') == 'farm':
        cashflow = random.randrange(10,21)
        session['userGold'] += cashflow
    if request.form.get('building') == 'cave':
        cashflow = random.randrange(5, 11)
        session['userGold'] += cashflow
    if request.form.get('building') == 'house':
        cashflow = random.randrange(2, 6)
        session['userGold'] += cashflow
    if request.form.get('building') == 'casino':
        cashflow = random.randrange(-51, 51)
        session['userGold'] += cashflow
    return redirect('/')

@app.route('/clear')
def restar():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)