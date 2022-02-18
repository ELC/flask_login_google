from flask import Blueprint, redirect, url_for

from flask_login import logout_user

login_blueprint = Blueprint("login", __name__)


@login_blueprint.get("/logout")
def hello():
    logout_user()
    return redirect(url_for("base.hello"))
