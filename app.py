from flask import Flask
from flask_smorest import Api

from api import register_api
from models import db


def create_app(config_obj: str):
    app = Flask(__name__, static_url_path="", static_folder="ui")
    app.config.from_object(config_obj)

    db.init_app(app)

    api = Api(app)
    register_api(api)

    return app


app = create_app("config.Config")


@app.route("/<path:path>")
def static_file(path):
    return app.send_static_file(path)


@app.route("/", methods=["GET"])
def redirect_to_index():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.config["DEBUG"] = True

    with app.app_context():
        db.create_all()

    app.run(port=5000)
