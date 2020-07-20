from flask import Flask

from todo.views import home_views

app = Flask(__name__)
app.register_blueprint(home_views.blueprint)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
