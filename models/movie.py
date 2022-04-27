from sqlalchemy import Table, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import mapper

def movie_model(db_session, metadata):

    class Movie(object):
        query = db_session.query_property()

        def __init__(self, title=None, director=None, starring=None, gene=None, release_date=None, running_time=None, synopsis=None, img_url=None):
            self.title = title
            self.director = director
            self.starring = starring
            self.genre = genre
            self.release_date = release_date
            self.running_time = running_time
            self.synopsis = synopsis
            self.img_url = img_url

        def __repr__(self):
            return f'<Movie {self.title!r}>'

    movies = Table('movies', metadata,
        Column('id', Integer, primary_key=True),
        Column('title', String(30), unique=False, nullable=False),
        Column('director', String(30), unique=False, nullable=False),
        Column('starring', String(300), unique=False),
        Column('genre', String(300), unique=False),
        Column('release_date', DateTime, unique=False),
        Column('running_time', String(30), unique=False),
        Column('synopsis', String(500), unique=False),
        Column('img_url', String(200), unique=False)
    )
    mapper(Movie, movies)
    return movies