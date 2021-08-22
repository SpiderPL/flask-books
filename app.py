from flask import Flask, escape, request
from flask_smorest import Api

from api import register_api
from models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DebugConfig")

    db.init_app(app)

    api = Api(app)
    register_api(api)

    return app


app = create_app()


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(port=5000)
