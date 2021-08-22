from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    authors = db.Column(db.String(80), unique=False, nullable=False)
    published_date = db.Column(db.Date, nullable=True)
    isbn = db.Column(db.String(80), unique=True, nullable=True)
    page_count = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String, nullable=True)

    def __repr__(self):
        return "<Title %r>" % self.title
