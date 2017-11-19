from flask import Flask
app = Flask(__name__)
app.secret_key = "flask123"

@app.route('/')
def index():
    return "hello world"

@app.route('/info')
def info():
    return "This is the info page"

app.run(debug=True)