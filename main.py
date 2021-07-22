from app import create_app

app = create_app()
@app.get("/status")
def status():
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)

