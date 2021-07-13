from enum import unique
from os import name
from flask import Flask
#from gevent import pywsgi
from flask_sqlalchemy import SQLAlchemy
import pymysql
import config
from sqlalchemy.orm import backref


pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(config)   #flask加载配置文件,，配置sqlalchemy
db = SQLAlchemy(app)
print(db)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.BigInteger, primary_key = True)
    name = db.Column(db.String(255), unique = True)

    users = db.relationship('User', backref = 'role')

    def __repr__(self):
        return 'Role: %s %s' % (self.id, self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.BigInteger, primary_key = True)
    name = db.Column(db.String(255), unique = True, index=True)
    mobile = db.Column(db.BigInteger, unique = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(255), unique = True)
    token = db.Column(db.String(255))
    token_expire = db.Column(db.DateTime(3))
    created_at = db.Column(db.DateTime(3))
    updated_at = db.Column(db.DateTime(3))
    deleted_at = db.Column(db.DateTime(3))

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return "User: %s %s %s %s %s %s %s %s %s %s %s" % (self.id, self.name, self.mobile, self.email, self.password,
                                                        self.token, self.token_expire, self.created_at,
                                                        self.updated_at, self.deleted_at, self.role_id)


@app.route("/")
def hello():
    return "hello world!"


if __name__ == '__main__':

    #db.drop_all()
    db.create_all()

    role = Role(name = "yin")
    db.session.add(role)
    db.session.commit()

    user = User(name = "ylolii", role_id = role.id)
    db.session.add(user)
    db.session.commit()
  
    app.run(debug=True)
    #server = pywsgi.WSGIServer(('0.0.0.0',(config.PORT)),app)
    #erver.serve_forever()