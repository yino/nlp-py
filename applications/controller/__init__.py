
from flask import Flask

from .qa import qaApp


def init_router(app: Flask):
    app.register_blueprint(qaApp)
