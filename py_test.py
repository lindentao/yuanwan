from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return '<h1>hello ,%s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)