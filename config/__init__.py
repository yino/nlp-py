import configparser
import os

config = configparser.ConfigParser()  # 类实例化

env = os.getenv("ENV")
env_path = os.getenv("CONFIG_PATH")
if env is None or len(env) == 0 or env == '':
    filename = "dev.ini"
else:
    filename = "%s.ini" % (env,)

if  env_path is None or len(env_path) == 0 or env_path == '':
    env_path = " D:\\project\\nlp-model"
print(env_path+"/"+filename)
config.read(env_path+"/"+filename,"utf8")
