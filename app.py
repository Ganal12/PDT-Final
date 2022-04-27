from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash
import re
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import engine, metadata, db_session, init_db
from models.user import user_model, user_list_model
from models.movie import movie_model
from models.article import article_model
from controllers.crud import crud_controller
from views.index import construct_index_bp
from views.login import construct_login_bp
from views.profile import construct_profile_bp
from views.movie import construct_movie_bp

#init models
user = user_model(db_session, metadata)
userList = user_list_model(db_session, metadata)
movie = movie_model(db_session, metadata)
article = article_model(db_session, metadata)

#init database
init_db()
conn = engine.connect()

user_control = crud_controller(conn, user)
user_list_control = crud_controller(conn, userList) 
movie_control = crud_controller(conn, movie) 
article_control = crud_controller(conn, article) 

index = construct_index_bp(user_control)
login = construct_login_bp(user_control)
profile = construct_profile_bp(user_control)
movies = construct_movie_bp(movie_control)

app = Flask(__name__,static_url_path='', static_folder='views/static',template_folder='views/templates')
app.secret_key = 'super secret key'

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(profile)
app.register_blueprint(movies)