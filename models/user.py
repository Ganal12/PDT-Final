from sqlalchemy import Table, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import mapper

def user_model(db_session, metadata):

    class User(object):
        query = db_session.query_property()

        def __init__(self, firstName=" ", lastName=" ", email=" ", password=" ", about_me=" ",user_type=1):
            self.status = status
            self.firstName = firstName
            self.lastName = lastName
            self.email = email
            self.password = password
            self.about_me = about_me
            self.user_type = user_type

        def __repr__(self):
            return f'<User {self.status!r}>'

    users = Table('users', metadata,
        Column('id', Integer, primary_key=True),
        Column('firstName', String(30), unique=False, nullable=False),
        Column('lastName', String(30), unique=False, nullable=False),
        Column('email', String(120), unique=False, nullable=False),
        Column('password', String(30), unique=False, nullable=False),
        Column('about_me', String(400), unique=False),
        Column('user_type', Integer, unique=False),
    )
    mapper(User, users)
    return users

def user_list_model(db_session, metadata):

    class UserList(object):
        query = db_session.query_property()

        def __init__(self, movie_id=None, is_watched=None, rating=None):
            self.movie_id = movie_id
            self.is_watched = is_watched
            self.rating = rating

        def __repr__(self):
            return f'<UserList {self.title!r}>'

    user_lists = Table('user_lists', metadata,
        Column('id', Integer, primary_key=True),
        Column('user_id', ForeignKey('users.id'), primary_key=True),
        Column('movie_id', ForeignKey('movies.id'), unique=False, nullable=False),
        Column('is_watched', Integer, unique=False, nullable=False),
        Column('rating', Integer, unique=False)
    )
    mapper(UserList, user_lists)
    return user_lists