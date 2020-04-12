from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("my_form_test.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['name_from_form'] = request.form['name']
    session['email_from_form'] = request.form['email']
    return redirect("/show")

@app.route('/show')
def show_results():
    return render_template("results.html", name_on_template=session['name_from_form'], email_on_template=session['email_from_form'])

if __name__ == "__main__":
    app.run(debug=True)