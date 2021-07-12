from flask import Flask
from gevent import pywsgi
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

db.create_all()

@app.route("/")
def hello():
    return "hello world!"

if __name__ == '__main__':
    #app.run(debug=True)
    server = pywsgi.WSGIServer(('',(config.PORT)),app)
    server.serve_forever()