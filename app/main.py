from flask import Flask, jsonify


def create_app(config, login_manager, external_blueprints=None):
    app = Flask(__name__)
    app.config.update(config)

    from app.routes import blueprints

    blueprints_to_add = blueprints[:]

    login_manager.init_app(app)

    if external_blueprints:
        blueprints_to_add += external_blueprints

    for blueprint, url_prefix in blueprints_to_add:
        app.register_blueprint(blueprint, url_prefix=url_prefix)

    return app
