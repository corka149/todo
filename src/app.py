import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    todos = get_todos()
    return flask.render_template('home/index.html', todos=todos)


@app.route('/about')
def about():
    return flask.render_template('home/about.html')


def get_todos():
    todos = [
        {'description': 'Cook', 'done': False},
        {'description': 'Clean', 'done': True}
    ]
    return todos


if __name__ == '__main__':
    app.run(debug=True)
