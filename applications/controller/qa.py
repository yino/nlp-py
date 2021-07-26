from applications import resp
from flask import Blueprint, g, jsonify

from ..service.qa import Qa

qaApp = Blueprint("qa",__name__,url_prefix="/qa")


@qaApp.route("/question_list")
def list():
    data = Qa.getListByUserId(g.user_id)
    return  resp.response(code=resp.SUCCESS, data=data)
