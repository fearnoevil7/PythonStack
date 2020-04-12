from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("the_dojo_survey.html")

@app.route('/users', methods=['POST'])
def submit_survey_info():
    print('Survey Received!!!!!!!')
    print(request.form)
    name_from_form = request.form['name']
    where_are_you = request.form['myLocation']
    que_dices = request.form['rap']
    anything_else = request.form['comments']
    return render_template("survey_results.html", nombre = name_from_form, posted= where_are_you, speakin_my_language= que_dices, final_thoughts= anything_else)

# @app.route('/Submit', methods=['POST'])
# def results_are_in():
#     return render_template("survery_results.html")

if __name__ == "__main__":
    app.run(debug=True)