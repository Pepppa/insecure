.PHONY: all docker docker-run

all: docker docker-run
	
docker:
	docker build .  -f docker/Dockerfile -t insecure

docker-run: docker
#	docker run -p 1234:5000 insecure
	docker run insecure

