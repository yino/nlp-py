
from app.controller.qa import qa
from flask import Flask


def init_route(app: Flask):
    app.register_blueprint(qa, url_prefix="/qa")
    