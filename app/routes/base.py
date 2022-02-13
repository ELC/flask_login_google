from flask import Blueprint, current_app, jsonify, redirect, url_for

from flask_dance.contrib.google import google

base = Blueprint("base", __name__)


@base.get("/")
def hello():
    return jsonify("hello, world!")


@base.get("/user")
def hello_user():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok, resp.text
    return jsonify("You are {email} on Google".format(email=resp.json()["email"]))


@base.get("/admin")
def hello_admin():
    return jsonify("hello, Admin!")
