.PHONY: docker-insecure docker-insecuredata insecure-run insecuredata-run

all: docker all-run

docker-insecure:
	docker build . -f docker/site/Dockerfile -t insecure

docker-insecuredata:
	docker build . -f docker/secure/Dockerfile -t insecuredata

docker: docker-insecure docker-insecuredata

insecure-run:
	kubectl apply -f k8s/site_depl.yaml
	kubectl apply -f k8s/site_service.yaml

insecuredata-run:
	docker run -d -v /home/admin:/home/admin -v /etc/passwd:/etc/passwd -v /etc/shadow:/etc/shadow --restart=always -p 3000:5001 insecuredata

all-run: insecure-run insecuredata-run

