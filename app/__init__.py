from flask import Flask
from app.routes.uf_route import uf_api
from flasgger import Swagger


def create_app(config):
    app = Flask(__name__)
    swagger = Swagger()
    app.register_blueprint(uf_api)
    app.config.from_object(config)
    app.app_context().push()
    swagger.init_app(app)
    return app
