from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    fruit_strawberry = request.form['strawberry']
    fruit_raspberry = request.form['raspberry']
    fruit_apple = request.form['apple']
    user_name = request.form['first_name']
    user_last = request.form['last_name']
    id_num = request.form['student_id']
    how_many = int(request.form['strawberry'])+ int(request.form['raspberry'])+ int(request.form['apple'])

    return render_template("checkout.html", fresa = fruit_strawberry, rpb = fruit_raspberry, manzana = fruit_apple, nombre = user_name, appolido = user_last, numero_id = id_num, count = how_many)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    