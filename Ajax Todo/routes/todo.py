from flask import render_template
from flask import Blueprint


from models import Todo


main = Blueprint('todo', __name__)


@main.route('/')
def index():
    todos = Todo.query.order_by('created_time desc').all()
    return render_template('index.html', todos=todos)
