from contextlib import suppress

from .main import create_app

from dotenv import dotenv_values
from flask_login import LoginManager
from flask_dance.contrib.google import make_google_blueprint

import os

with suppress(ImportError):
    from rich.traceback import install
    install(show_locals=True)


def init():
    config = os.environ.copy()
    config.update(dotenv_values(".env"))

    login_manager = LoginManager()

    google_scopes = [
        "https://www.googleapis.com/auth/userinfo.email", 
        "openid", 
        "https://www.googleapis.com/auth/userinfo.profile"
    ]
    google_bp = make_google_blueprint(scope=google_scopes, redirect_to="base.hello_user")

    external_blueprints = [
        (google_bp, "/login")
    ]

    return create_app(config, login_manager, external_blueprints)

app = init()
