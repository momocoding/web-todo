from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import time
import json


app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(app)


class ModelHelper(object):
    def __repr__(self):
        """
        __repr__ 是一个魔法方法
        简单来说, 它的作用是得到类的 字符串表达 形式
        比如 print(u) 实际上是 print(u.__repr__())
        """
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} \n>\n'.format(classname, s)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format_time(self, t):
        format = '%Y/%m/%d %H:%M:%S'
        value = time.localtime(int(time.time()))
        dt = time.strftime(format, value)
        return dt


class Todo(db.Model, ModelHelper):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())
    created_time = db.Column(db.String())

    def __init__(self, form):
        self.task = form.get('task', '')
        self.created_time = self.format_time(int(time.time()))

    def to_dict(self):
        d = dict(
            id=self.id,
            task=self.task,
            created_time=self.created_time,
        )
        return d


if __name__ == '__main__':
    # 先 drop_all 删除所有数据库中的表
    # 再 create_all 创建所有的表
    db.drop_all()
    db.create_all()
    print('rebuild database')