from flask import Blueprint, current_app, jsonify, redirect, url_for, render_template

from flask_dance.contrib.google import google

from app.models import User

base_blueprint = Blueprint("base", __name__)


@base_blueprint.get("/")
def hello():
    return jsonify("hello, world!")


@base_blueprint.get("/user")
def hello_user():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v1/userinfo")

    if not resp.ok or not resp.text:
        raise ValueError("A problem occured during log in")

    user_json = resp.json()
    logged_user = User(
        profile_pic=user_json["picture"],
        name=user_json["name"],
        email=user_json["email"],
    )

    return render_template("user_card.html", user=logged_user)


@base_blueprint.get("/user_test")
def hello_user_test():
    user_json = {
        "email": "skielcast@gmail.com",
        "name": "Ezequiel L. Castaño",
        "picture": "https://lh3.googleusercontent.com/a-/AOh14Gh-y3JoTkER7OqlMNv7NhbuAijOSVMzVxDli8xtxeo=s96-c",
    }
    logged_user = User(
        profile_pic=user_json["picture"],
        name=user_json["name"],
        email=user_json["email"],
    )
    return render_template("user_card.html", user=logged_user)


@base_blueprint.get("/admin")
def hello_admin():
    return jsonify("hello, Admin!")
