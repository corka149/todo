import flask

from todo.infrastructure.view_modifiers import response
from todo.services import todo_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def hello_world():
    return {'todos': todo_service.get_todos()}


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
