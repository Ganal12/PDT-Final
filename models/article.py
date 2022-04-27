from sqlalchemy import Table, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import mapper

def article_model(db_session, metadata):

    class Article(object):
        query = db_session.query_property()

        def __init__(self, title=None, message=None, posted_date=None, types=None, is_deleted=None,):
            self.title = title
            self.message = message
            self.posted_date = posted_date
            self.type = types
            self.is_deleted = is_deleted

        def __repr__(self):
            return f'<Article {self.title!r}>'

    articles = Table('articles', metadata,
        Column('id', Integer, primary_key=True),
        Column('title', String(30), unique=False, nullable=False),
        Column('message', String(30), unique=False, nullable=False),
        Column('posted_date', DateTime, unique=False),
        Column('type', Integer, unique=False),
        Column('is_deleted', Integer, unique=False),
    )
    mapper(Article, articles)
    return articles