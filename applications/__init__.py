from config import init_config
from flask import Flask

from .controller import init_router
from .middleware import init_middleware
from .model import init_db


def create_app():
    app = Flask(__name__)
    init_config()
    init_db(app)
    init_router(app)
    init_middleware(app)
    return app
