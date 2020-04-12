from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('checkerboard.html', rows = 4,
    columns = 8)

@app.route('/<x>')
def index1(x):
    return render_template('checkerboard.html', rows = int(x), columns= 8)

@app.route('/<x>/<j>')
def index2(x, j):
    return render_template('checkerboard.html', rows = int(x), columns = int(j))

if(__name__ == "__main__"):
    app.run(debug=True)