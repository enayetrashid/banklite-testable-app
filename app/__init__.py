from flask import Flask

from app.api.routes import api_bp
from app.repositories.storage import InMemoryStorage
from app.web.routes import web_bp


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-key"
    app.config["STORAGE"] = InMemoryStorage()

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)

    return app
