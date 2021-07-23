from flask import Blueprint, g, jsonify

from ..service.qa import Qa

qaApp = Blueprint("qa",__name__,url_prefix="/qa")


@qaApp.route("/question_list")
def list():
    Qa.getListByUserId(g.user_id)
    return 1
