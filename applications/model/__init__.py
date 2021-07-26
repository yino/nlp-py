# 注册db
import pymysql
from config import mysql
from flask import Flask, request
from flask_sqlalchemy import BaseQuery, SQLAlchemy

pymysql.install_as_MySQLdb()

class Query(BaseQuery):
     def layui_paginate(self):
        """
        layui表格分页
        page
        limit
        """
        return self.paginate(page=request.args.get('page', type=int),
                             per_page=request.args.get('limit', type=int),
                             error_out=False)
db = SQLAlchemy(query_class=Query)

def init_db(app: Flask):
    app.config.from_object(mysql)
    db.init_app(app)
