from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    userHtml = [
        {'First Name' : 'Michael', 'Last Name' : 'Choi'},
        {'First Name' : 'John', 'Last Name' : 'Supsupin'},
        {'First Name' : 'Mark', 'Last Name' : 'Guillen'},
        {'First Name' : 'KB', 'Last Name' : 'Tonel'}
    ]
    return render_template("htmlTable.html", user_info= userHtml)


if (__name__ == "__main__"):
    app.run(debug = True)