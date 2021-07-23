from flask import Flask, g, jsonify, request

from ..service.user import User


def init_middleware(app: Flask):
    
    @app.before_request
    def before_request():
        ak = request.args.get("ak")
        if ak is None:
            return jsonify({
                "code": "-1",
                "message": "参数错误",
            })
        
        userInfo = User.getUserInfoByAk(ak)
        if userInfo is None:
             return jsonify({
                "code": "-1",
                "message": "无效的 ak",
            })
        g.user_id = userInfo.user_id
        return None


