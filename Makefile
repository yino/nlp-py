run:
	python main.py

build:
	docker-compose build

start:
	docker-compose up
	
gunicorn:
	gunicorn -c gunicorn.conf.py main:app  --preload

up:
	docker-compose up -d
	
