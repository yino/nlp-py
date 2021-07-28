from applications import resp
from flask import Blueprint, g, jsonify, request

from ..service import qa

qaApp = Blueprint("qa",__name__,url_prefix="/qa")

Qa = qa.Qa()
@qaApp.route("/question_list")
def list():
    data = Qa.getListByUserId(g.user_id)
    return  resp.response(code=resp.SUCCESS, data=data)

@qaApp.route("/train_model")
def train():
    res = Qa.trainModel(user_id=g.user_id)
    print(res)
    if not res:
        return resp.response(code=resp.ERROR_TRAIN_MODEL)
    return  resp.response(code=resp.SUCCESS)

@qaApp.route("/match")
def match():
    question = request.args.get("question")
    res = Qa.match(user_id=g.user_id, input_question=question)
    return  resp.response(code=resp.SUCCESS, data=res)
