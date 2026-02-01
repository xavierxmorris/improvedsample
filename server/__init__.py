from flask import Flask
from server.routes.publishers import publishers_bp

def create_app(config_name: str = 'default') -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_name)
    app.register_blueprint(publishers_bp)
    return app