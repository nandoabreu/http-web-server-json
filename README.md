# http-web-server-json

Basic scaled HTTP server responding GET and POST with JSON. This project was designed for development testing proposal.

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
