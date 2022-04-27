from flask import Flask, redirect, jsonify, render_template, url_for, session, request, flash, Blueprint
import sys

def construct_profile_bp(controller):
    profile_bp = Blueprint('profile', __name__,static_folder='static',template_folder='templates')

    @profile_bp.route("/profile")
    def profile():
        user_id = session.get('uId')

        profile = controller.get("id = %s" % (user_id)).fetchone()

        print(profile, file=sys.stdout)

        return render_template('profile/profile.html', uData=profile)
    return profile_bp