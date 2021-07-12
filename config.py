#encoding: utf-8

#dialect+driver://username:password@host:port/database
DIALECT = 'mysql' #数据库，如 MYSQL、SQLite、PostgreSQL并且转换成小写
DRIVER = 'mysqldb'  #python对应的驱动，如果不指定，回默认选择，mysql的默认驱动是mySQLdb
USERNAME = 'nlp-cb' #连接数据库的用户名
PASSWORD = 'cb123456' #连接数据库的密码
HOST = '124.70.70.45'    #连接数据库的域名
PORT = '3306'   #数据库监听的端口号
DATEBASE = 'nlp' #连接数据库的名字

SQLALCHEMY_DATEBASE_URI = "{}:{}//{}:{}@{}:{}/{}?harset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATEBASE)
print(SQLALCHEMY_DATEBASE_URI)

SQLALCHEMY_TRACK_MODIFICATIONS = False
