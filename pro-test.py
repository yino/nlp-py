from datetime import datetime
from enum import unique
from os import name

import pymysql
from flask import Flask
from flask.sessions import NullSession
#from gevent import pywsgi
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, defaultload
from sqlalchemy.sql.elements import Null
from werkzeug.datastructures import UpdateDictMixin

import config

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(config)   #flask加载配置文件,，配置sqlalchemy
db = SQLAlchemy(app)

class User_appkey(db.Model):
    __tablename__ = "user_appkey"
    id = db.Column(db.BigInteger,primary_key = True)
    app_key = db.Column(db.String(255), unique = True)
    app_secret = db.Column(db.String(255), unique = True)
    type = db.Column(db.String(20))
    req_num = db.Column(db.BigInteger)
    user_id = db.Column(db.BigInteger,  primary_key = True)
    created_at = db.Column(db.DateTime(3))
    updated_at = db.Column(db.DateTime(3))
    deleted_at = db.Column(db.DateTime(3))

    def __repr__(self):
       return self.name

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.BigInteger, primary_key = True, nullable=False)
    name = db.Column(db.String(255), )
    mobile = db.Column(db.BigInteger, unique = True, nullable=False)
    email = db.Column(db.String(100), nullable = True)
    password = db.Column(db.String(255), nullable=False)
    token = db.Column(db.String(255), nullable = True)
    token_expire = db.Column(db.DateTime(3), default = datetime.now, nullable=False)
    created_at = db.Column(db.DateTime(3), default = datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime(3), default = datetime.now, nullable=False)
    deleted_at = db.Column(db.DateTime(3), default = datetime.now, nullable = True)

    def __repr__(self):
        return self.name


class Qa_question(db.Model):
    __tablename__ = "qa_questions"
    id = db.Column(db.BigInteger, primary_key = True)
    question = db.Column(db.String(255))
    answer = db.Column(db.String(255))
    pid = db.Column(db.Integer, unique = True)
    user_id = db.Column(db.BigInteger)
    type = db.Column(db.BigInteger)
    created_at = db.Column(db.DateTime(3))
    updated_at = db.Column(db.DateTime(3))
    deleted_at = db.Column(db.DateTime(3))

    def __repr__(self):
        return self.name


@app.route("/")
def hello():
    return "hello world!"


def GetUserId(Ak, As):
    data = User_appkey.query.filter(User_appkey.app_key==Ak).filter(User_appkey.app_secret==As).first()
    
    print(data)

if __name__ == '__main__':

    #print (datetime.strftime(nowTime, '%Y-%m-%d %H:%M:%S.%f'))
    # user = User(name = "yoloii", mobile = "15829002364", email = "123456@163.com", password = "qwertyuiop", token = "whatmean", token_expire = nowTime, 
    #                  created_at = nowTime, updated_at = nowTime, deleted_at = nowTime)
    # db.session.add(user)
    # db.session.commit()

    #删除：查出要删除的数据，拿到Article
    #result = User.query.filter(User.id==8).first()
    #db.session.delete(result)
    #db.session.commit()

    # all = User.query.all()
    # print(all)
    # cou = User.query.count()
    # print(cou)
    GetUserId(Ak="3e76e966f02f8b821e0402829b4f0a571",As="f74fd7a13cd98b1aa53d02b7efc10694")
    # app.run(debug=True)
    #server = pywsgi.WSGIServer(('0.0.0.0',(config.PORT)),app)
    #erver.serve_forever()
