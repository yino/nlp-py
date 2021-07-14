from datetime import datetime
from enum import unique
from os import name
from flask import Flask
from flask.sessions import NullSession
#from gevent import pywsgi
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy.sql.elements import Null
from werkzeug.datastructures import UpdateDictMixin
import config
from sqlalchemy.orm import backref, defaultload
from datetime import datetime


pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(config)   #flask加载配置文件,，配置sqlalchemy
db = SQLAlchemy(app)
print(db)

class User_appkey(db.Model):
    __tablename__ = "user_appkey"
    id = db.Column(db.BigInteger)
    app_key = db.Column(db.String(255), unique = True)
    app_secret = db.Column(db.String(255), unique = True)
    user_id = db.Column(db.BigInteger,  primary_key = True)
    created_at = db.Column(db.DateTime(3))
    updated_at = db.Column(db.DateTime(3))
    deleted_at = db.Column(db.DateTime(3))

    def __repr__(self):
        return "User_appkey: %s %s %s %s %s %s %s" % (self.id, self.app_key, self.app_secret, 
                                                        self.user_id, self.created_at, self.updated_at,self.deleted_at)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.BigInteger, primary_key = True, nullable=False)
    name = db.Column(db.String(255), unique = True)
    mobile = db.Column(db.BigInteger, unique = True, nullable=False)
    email = db.Column(db.String(100), nullable = True)
    password = db.Column(db.String(255), unique = True, nullable=False)
    token = db.Column(db.String(255), nullable = True)
    token_expire = db.Column(db.DateTime(3), default = datetime.now, nullable=False)
    created_at = db.Column(db.DateTime(3), default = datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime(3), default = datetime.now, nullable=False)
    deleted_at = db.Column(db.DateTime(3), default = datetime.now, nullable = True)

    def __repr__(self):
        return "User: %s %s %s %s %s %s %s %s %s %s" % (self.id, self.name, self.mobile, self.email, self.password,
                                                            self.token, self.token_expire, self.created_at,
                                                            self.updated_at, self.deleted_at)


class Qa_question(db.Model):
    __tablename__ = "qa_questions"
    id = db.Column(db.BigInteger)
    question = db.Column(db.String(255), unique = True)
    answer = db.Column(db.String(255), unique = True)
    pid = db.Column(db.Integer, unique = True)
    user_id = db.Column(db.BigInteger, primary_key = True)
    type = db.Column(db.BigInteger)
    created_at = db.Column(db.DateTime(3))
    updated_at = db.Column(db.DateTime(3))
    deleted_at = db.Column(db.DateTime(3))

    def __repr__(self):
        return "Qa_question: %s %s %s %s %s %s %s %s %s" % (self.id, self.question, self.answer, self.pid,
                                                                self.user_id, self.type, self.created_at,
                                                                self.updated_at, self.deleted_at)


@app.route("/")
def hello():
    return "hello world!"


if __name__ == '__main__':

    #db.drop_all()
    #db.create_all()
 
    nowTime = datetime.now()
    print (nowTime)
    #print (datetime.strftime(nowTime, '%Y-%m-%d %H:%M:%S.%f'))
    user = User(name = "yoloii", mobile = "15829002364", email = "123456@163.com", password = "qwertyuiop", token = "whatmean", token_expire = nowTime, 
                     created_at = nowTime, updated_at = nowTime, deleted_at = nowTime)
    db.session.add(user)
    db.session.commit()

    #删除：查出要删除的数据，拿到Article
    #result = User.query.filter(User.id==8).first()
    #db.session.delete(result)
    #db.session.commit()

    all = User.query.all()
    print(all)
    cou = User.query.count()
    print(cou)

    app.run(debug=True)
    #server = pywsgi.WSGIServer(('0.0.0.0',(config.PORT)),app)
    #erver.serve_forever()