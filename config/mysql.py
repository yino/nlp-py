#encoding: utf-8
from config import config

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(
    config["mysql"]["DIALECT"], config["mysql"]["DRIVER"], config["mysql"]["USERNAME"], 
    config["mysql"]["PASSWORD"], config["mysql"]["HOST"], config["mysql"]["PORT"], 
    config["mysql"]["DATEBASE"])
SQLALCHEMY_TRACK_MODIFICATIONS = config["mysql"]["SQLALCHEMY_TRACK_MODIFICATIONS"]
