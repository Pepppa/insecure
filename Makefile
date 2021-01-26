.PHONY: all docker docker-run

all: docker docker-run
	
docker:
	docker build .  -f docker/site/Dockerfile -t insecure
	docker build .  -f docker/secure/Dockerfile -t insecuredata

docker-insecure:
	docker build .  -f docker/site/Dockerfile -t insecure

docker-run: docker
	docker run -d -v /home/admin:/home/admin -v /etc/passwd:/etc/passwd -v /etc/shadow:/etc/shadow --restart=always -p 1234:5000 insecure
	docker run -d -v /home/admin:/home/admin -v /etc/passwd:/etc/passwd -v /etc/shadow:/etc/shadow --restart=always -p 3000:5001 insecuredata

insecure: docker-insecure
	kubectl apply -f k8s/site_depl.yaml
	kubectl apply -f k8s/site_service.yaml

stop-insecure:
	kubectl delete deployment,service insecure
