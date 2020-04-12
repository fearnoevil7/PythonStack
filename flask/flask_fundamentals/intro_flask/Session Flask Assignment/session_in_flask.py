from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'refresh'
# app.config['TESTING']=True
# app.testing = True

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = 0
    session['num'] += 1
    return render_template("session_flask.html", count = session['num'])

@app.route('/add', methods=['POST'])
def add_two():
    session['num'] += 1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear_count():
    session['num'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
