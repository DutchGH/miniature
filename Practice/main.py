from flask import Flask, request,
from flask_wtf import Form
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return 'Your browser is %s' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!<h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
