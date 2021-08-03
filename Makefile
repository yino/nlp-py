Project := nlp-model

run:
	python main.py

build:
	docker-compose build

start:
	docker-compose up
	
#gunicorn -c $(Project)/gunicorn.conf.py main:app  --preload
up:
	docker-compose up -d

bash:
	docker-compose exec nlp-py bash
