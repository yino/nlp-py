# 注册db
import pymysql
from config import mysql
# from config.mysql import SQLALCHEMY_DATABASE_URI
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

def init_db(app: Flask):
    app.config.from_object(mysql)
    db = SQLAlchemy(app)
    return db
