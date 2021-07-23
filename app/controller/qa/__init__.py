from flask import Blueprint, jsonify

qa=Blueprint('qa',__name__)

# 注册路由
from .route import *
