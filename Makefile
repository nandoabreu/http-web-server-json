IMAGE=rest-json
SERVICE=rest-json
PORT=5000
SCALE=3

start:
	docker-compose up -d --scale ${SERVICE}=${SCALE}

test:
	curl -H "Content-Type: application/json" http://0.0.0.0:${PORT}/
	@echo
	curl -X POST -H "Content-Type: application/json" -d '{"name": "Fernando Abreu", "GitHub": "nandoabreu"}' http://0.0.0.0:${PORT}/
	@echo

logs:
	docker-compose logs -t -f

stop:
	docker-compose down

default: start
