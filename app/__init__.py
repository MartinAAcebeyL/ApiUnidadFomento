from flask import Flask
from app.routes.uf_route import uf_api

def create_app(config):
    app = Flask(__name__)
    app.register_blueprint(uf_api)
    app.config.from_object(config)
    app.app_context().push()
    return app
