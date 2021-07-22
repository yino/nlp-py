from flask import Flask
from model import init_db

from app.controller import init_route

app = Flask(__name__)
db = init_db(app)
init_route(app)

def create_app():
    return app
