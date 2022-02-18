from .base import base_blueprint
from .login import login_blueprint

blueprints = [(base_blueprint, "/"), (login_blueprint, "/")]
