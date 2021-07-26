from flask import jsonify
from pymysql import STRING

SUCCESS = 200 # 成功
ERROR_PARAMS = 40001 #参数错误
ERROR_PARAMS_TOKEN = 40002 #无效的token参数
ERROR_TOKEN = 50001 # token 有误

def response(code, data="",message=""):
    return jsonify({
        "code": code,
        "data": data,
        "message": resp_code(code)+" "+message
    })

def resp_code(code)->STRING:
    data = {}
    data[SUCCESS] = "success"
    data[ERROR_PARAMS] = "error auth params "
    data[ERROR_PARAMS_TOKEN] = "please input token"
    data[ERROR_TOKEN] = "token fail"

    if code in data == False:
        return ''
    return data[code]
    