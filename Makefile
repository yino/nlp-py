Project := nlp-model

run:
	python main.py

build:
	sudo docker-compose build

start:
	sudo docker-compose up

stop:
	sudo docker-compose stop
	
#gunicorn -c $(Project)/gunicorn.conf.py main:app  --preload
up:
	sudo docker-compose up -d

bash:
	sudo docker-compose exec nlp-py bash
