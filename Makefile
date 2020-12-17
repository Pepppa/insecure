.PHONY: all docker docker-run

all: docker docker-run
	
docker:
	docker build .  -f docker/site/Dockerfile -t insecure
	docker build .  -f docker/secure/Dockerfile -t insecuredata

docker-run: docker
#	docker run -p 1234:5000 insecure
	docker run -d -v /home/admin:/home/admin -v /etc/passwd:/etc/passwd -v /etc/shadow:/etc/shadow --restart=always -p 1234:5000 insecure
	docker run -d -v /home/admin:/home/admin -v /etc/passwd:/etc/passwd -v /etc/shadow:/etc/shadow --restart=always -p 3000:5001 insecuredata
#	docker run insecure

