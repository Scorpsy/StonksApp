from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/introduction")
def introduction():
    return "Hello Matthew desu"

if __name__ == '__main__':
    app.run()