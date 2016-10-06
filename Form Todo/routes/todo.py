from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import abort


from models import Todo


main = Blueprint('todo', __name__)


@main.route('/')
def index():
    todos = Todo.query.order_by('created_time desc').all()
    return render_template('index.html', todos=todos)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    t = Todo(form)
    if len(t.task) == 0 or len(t.task) > 50:
        abort(404)
    else:
        t.save()
        todos = Todo.query.order_by('created_time desc').all()
        return render_template('index.html', todos=todos)


@main.route('/delete/<int:todo_id>')
def delete(todo_id):
    t = Todo.query.get(todo_id)
    if t is None:
        return redirect(url_for('todo.index'))
    t.delete()
    todos = Todo.query.order_by('created_time desc').all()
    return render_template('index.html', todos=todos)


@main.route('/update/<int:todo_id>', methods=['POST'])
def update(todo_id):
    task = request.form.get('task', '')
    t = Todo.query.get(todo_id)
    if len(task) == 0 or len(task) > 50:
        abort(404)
    else:
        t.task = task
        t.save()
        todos = Todo.query.order_by('created_time desc').all()
        return render_template('index.html', todos=todos)


@main.route('/edit/<int:todo_id>')
def edit_view(todo_id):
    t = Todo.query.get(todo_id)
    return render_template('edit.html', todo=t)
