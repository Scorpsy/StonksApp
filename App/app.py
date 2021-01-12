from flask import Flask, request, render_template

app = Flask(__name__)

#TODO:
#need to make either google extension or webpage
#

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