from flask import Flask, jsonify


def create_app(config, login_manager, external_blueprints=None):
    app = Flask(__name__)
    app.config.update(config)

    from app.routes.base import base
    app.register_blueprint(base)
    login_manager.init_app(app)

    if external_blueprints:
        for blueprint, url_prefix in external_blueprints:
            app.register_blueprint(blueprint, url_prefix=url_prefix)

    return app
