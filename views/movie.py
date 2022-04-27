from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint

def construct_movie_bp(controller):
    movie_bp = Blueprint('movie', __name__,static_folder='static',template_folder='templates')

    @movie_bp.route("/movie/<id>")
    def movie(id):
        # print(controller.get("id=1"), file=sys.stdout) 
        # insObj = {"status":0,
        #     "firstName":'admin',
        #     "lastName":'admin',
        #     "email":'admin@admin.com',
        #     "password":'admin',
        #     "major":1}
        # print(controller.insert(insObj), file=sys.stdout)
        return render_template('movie/movie.html')
    
    @movie_bp.route("/movie/add", methods=['GET','POST'])
    def add():
        if request.method == 'POST':
            # email = request.form['email']
            # password = request.form['password']
            print(request.form)
        return render_template('movie/add.html')

    return movie_bp