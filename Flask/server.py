from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "flask123"

@app.route('/')
def index():
    return render_template('index.html')"

@app.route('/info')
def index():
    return render_template('form.html')

@app.route('/process', methods=["POST"])
def process():
    session["favorite_language"] = request.form["favorite_language"]
    # return render_template("form_information.html", x=request.for["favorite_language"], y =request.form["first_name"], z=request.form["last_name"])
    return redirect('/display_info')

@app.route('/display_info')
def display_info():
return render_template('display_info')

app.run(debug=True)