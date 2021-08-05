from gevent.pywsgi import WSGIServer

from applications import create_app
from config import config

app = create_app()
@app.get("/status")
def status():
    return "ok"

if __name__ == '__main__':
    # http_server = WSGIServer(('', int(config["app"]["PORT"])), app)
    # http_server.serve_forever()
    app.run(debug=config['app']['DEBUG'],host=config["app"]["HOST"], port=config["app"]["PORT"])

