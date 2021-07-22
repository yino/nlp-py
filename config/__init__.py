import configparser
import os

config = configparser.ConfigParser()  # 类实例化
env = os.getenv("env")
if len(env) == 0 or env == '':
    filename = "dev.ini"
else:
    filename = "%s.ini" % (env,)
config.read('D:\project\\nlp-model\\'+filename,"utf8")
