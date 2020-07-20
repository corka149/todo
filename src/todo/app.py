from flask import Flask

app = Flask(__name__)


def register_blueprints():
    from todo.views import home_views
    app.register_blueprint(home_views.blueprint)


def main():
    register_blueprints()
    app.run(debug=True)


if __name__ == '__main__':
    main()
