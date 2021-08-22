from flask.views import MethodView
from flask_smorest import Blueprint

from api.books.models import BooksGetQuery, Book
from models import Book as BookModel, db

blp = Blueprint(
    "recipes", "recipes", url_prefix="/api/books", description="Operations on books"
)


@blp.route("/")
class Recipes(MethodView):
    @blp.arguments(BooksGetQuery, location="query")
    @blp.response(200, Book(many=True))
    def get(self, args: dict):
        # """List all books"""
        limit = args["limit"]
        offset = args["offset"]

        books = BookModel.query.offset(offset).limit(limit).all()

        return books

    @blp.arguments(Book)
    @blp.response(201, Book)
    def post(self, args: dict):
        # """Post a book"""

        new_book = BookModel(**args)

        db.session.add(new_book)
        db.session.commit()

        return new_book
