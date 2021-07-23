from app import app
from flask import jsonify, request


@app.before_request
def before_request():
    Ak = request.args.get("ak")
    As = request.args.get("as")
    return None
       