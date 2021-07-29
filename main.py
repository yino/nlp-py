from applications import create_app
from config import config

app = create_app()
@app.get("/status")
def status():
    return "ok"

if __name__ == '__main__':
    app.run(debug=config['app']['DEBUG'],host=config["app"]["HOST"], port=config["app"]["PORT"])

