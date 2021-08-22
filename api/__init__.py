from flask_smorest import Api

from api.books import blp as books_blp


def register_api(api: Api):
    api.register_blueprint(books_blp)
