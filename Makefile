run:
	python main.py

build:
	pip install -r requirements.txt && python3 main.py

docker:
	docker-compose up
	
gunicorn:
	gunicorn -c gunicorn.config.py applications:applications