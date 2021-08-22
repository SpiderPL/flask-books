import os
import tempfile
import datetime

import pytest

from app import create_app
from models import db, Book


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app("config.TestConfig")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def db_client():
    return db


def test_index(client):
    rv = client.get("/index.html")
    assert b"Flask Library" in rv.data


def test_get_books(client):
    rv = client.get("/api/books/")

    assert rv.status_code == 200
    assert [] == rv.json


def test_get_one_book(client, db_client):
    db_client.session.add(
        Book(
            title="Harry Potter and the Chamber of Secrets",
            authors="J. K. Rowling",
            published_date=datetime.date(2015, 10, 5),
        )
    )
    db_client.session.commit()

    rv = client.get("/api/books/")

    assert rv.status_code == 200
    assert [
        {
            "authors": "J. K. Rowling",
            "id": 1,
            "image": None,
            "isbn": None,
            "page_count": None,
            "published_date": "2015-10-05",
            "title": "Harry Potter and the Chamber of Secrets",
        }
    ] == rv.json


def test_post_one_book(client, db_client):
    rv = client.post(
        "/api/books/",
        json={
            "authors": "Stephen King",
            "title": "The Shining",
            "published_date": "2011-10-05",
        },
        headers={"Content-Type": "application/json"},
    )

    assert rv.status_code == 201

    assert {
        "authors": "Stephen King",
        "id": 1,
        "image": None,
        "isbn": None,
        "page_count": None,
        "published_date": "2011-10-05",
        "title": "The Shining",
    } == rv.json

    books = Book.query.all()

    assert len(books) == 1
    assert books[0].id == 1
    assert books[0].title == "The Shining"
    assert books[0].authors == "Stephen King"
    assert books[0].published_date == datetime.date(2011, 10, 5)
