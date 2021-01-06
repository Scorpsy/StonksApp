from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('picture.html')

@app.route("/introduction")
def introduction():
    return "Hello Matthew desu"

@app.route("/mainpage")
def main_page():
    return render_template('picture.html')

if __name__ == '__main__':
    app.run()