from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>/')
def say(name):
    return "Hi " + name.capitalize() + "!"

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    return int(num) * word
if(__name__ == "__main__"):
    app.run(debug=True)