# http-web-server-json

Basic scaled HTTP server responding GET and POST with JSON. This project was designed for development testing proposal.

## Requirements
- Docker  
- Docker compose  
- curl (optional)

## Initiate

```
make start
make test
```

## Usage
```
curl -H "Content-Type: application/json" http://0.0.0.0:5000/
curl -X POST -H "Content-Type: application/json" -d '{"name": "Fernando Abreu", "GitHub": "nandoabreu"}' http://0.0.0.0:5000/

```

Or open a browser and navigate to http://localhost:5000/


## Expected response patterns
```
curl -H "Content-Type: application/json" http://0.0.0.0:5000/
{"response_at": "2021-03-20 20:41:34.829849", "response_from": "worker_hostname"}
```
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "Fernando Abreu", "GitHub": "nandoabreu"}' http://0.0.0.0:5000/
{"name": "Fernando Abreu", "GitHub": "nandoabreu", "received_at": "2021-03-20 20:41:34.847726", "received_from": "worker_hostname"}
```

## Logs
```
make logs
```

## Stop
```
make stop
```

## License
[MIT](LICENSE)
