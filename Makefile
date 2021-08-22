pip-compile:
	pip-compile --output-file=requirements.txt requirements.in

pip-install:
	 pip install -r requirements.txt

docker-up:
	docker-compose up

test:
	pytest .

.PHONY: test

fmt:
	black .