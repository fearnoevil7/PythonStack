from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello my friend!!!!!!!"

@app.route('/play')
def play():
    return render_template('playground.html', box_amount = 3, color="blue")

@app.route('/play/<num>')
def play1(num):
    return render_template('playground.html', box_amount = int(num), color="blue")

@app.route('/play/<num>/<type>')
def play2(num, type):
    return render_template('playground.html', box_amount = int(num), color = type) 
    # front end name = back end name

if(__name__ == "__main__"):
    app.run(debug=True)