import marshmallow as ma


class BooksGetQuery(ma.Schema):
    limit = ma.fields.Integer(missing=10)
    offset = ma.fields.Integer(missing=0)
    short = ma.fields.Integer(missing=0)
    q = ma.fields.List(ma.fields.Str, missing=[])


class Book(ma.Schema):
    id = ma.fields.Integer()
    title = ma.fields.String()
    authors = ma.fields.String()
    published_date = ma.fields.Date()
    isbn = ma.fields.String()
    page_count = ma.fields.Integer()
    image = ma.fields.String()
