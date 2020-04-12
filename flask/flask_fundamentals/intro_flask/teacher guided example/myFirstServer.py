from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/buzz')
def buzz():
    return "To infinity and beyond!"

@app.route('/sayhi/zach')
def sayhizach():
    return "Toy Story 4 life"

@app.route('/sayhi/<name>/')
def sayhi(name):
    return "Hello " + name 

if(__name__ == "__main__"):
    app.run(debug=True)