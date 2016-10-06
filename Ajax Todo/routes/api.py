from flask import request
from flask import Blueprint
import json

from models import Todo


main = Blueprint('api', __name__)


def response(success, data=None, message=''):
    r = dict(
        success=success,
        data=data,
        message=message
    )
    return json.dumps(r, ensure_ascii=False)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    t = Todo(form)
    if len(t.task) == 0:
        r = response(False, message='Todo不能为空')
    elif len(t.task) > 50:
        r = response(False, message='Todo不能大于50字')
    else:
        t.save()
        r = response(True, data=t.to_dict(), message='添加Todo成功')
    return r


@main.route('/delete/<int:todo_id>')
def delete(todo_id):
    t = Todo.query.get(todo_id)
    t.delete()
    r = response(True, message='Todo删除成功')
    return r


@main.route('/update/<int:todo_id>', methods=['POST'])
def update(todo_id):
    task = request.form.get('task', '')
    t = Todo.query.get(todo_id)
    t.task = task
    if len(t.task) == 0:
        r = response(False, message='Todo不能为空')
    elif len(t.task) > 50:
        r = response(False, message='Todo不能大于50字')
    else:
        t.save()
        r = response(True, data=t.to_dict(), message='更改成功')
    return r
