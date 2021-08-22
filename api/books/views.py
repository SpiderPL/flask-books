from flask.views import MethodView
from flask_smorest import Blueprint
from api.books.models import BooksGetQuery, Book
from models import Book as BookModel

blp = Blueprint(
    "recipes", "recipes", url_prefix="/api/books", description="Operations on books"
)


@blp.route("/")
class Recipes(MethodView):
    @blp.arguments(BooksGetQuery, location="query")
    @blp.response(200, Book(many=True))
    def get(self, args: BooksGetQuery):
        # """List all books"""
        limit = args["limit"]
        offset = args["offset"]

        books = BookModel.query.limit(limit).all()

        print(limit)

        return Book(many=True).dump(books)
