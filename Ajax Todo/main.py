from flask import Flask
from flask import render_template


from routes.todo import main as todo_routes
from routes.api import main as api_routes


app = Flask(__name__)
app.secret_key = 'random string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.register_blueprint(todo_routes)
app.register_blueprint(api_routes, url_prefix='/api')


@app.errorhandler(404)
def error404(e):
    return render_template('404.html')


if __name__ == '__main__':
    config = {
        'port': 3000,
        'debug': True,
    }
    app.run(**config)