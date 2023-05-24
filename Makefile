.PHONY: docker-insecure docker-insecuredata insecure-run insecuredata-run reinit-db collect-logs restart

all: docker all-run

docker-insecure:
	docker build . -f docker/site/Dockerfile -t insecure --network=host

docker-insecuredata:
	docker build . -f docker/secure/Dockerfile -t insecuredata --network=host

docker: docker-insecure docker-insecuredata

insecure-run:
	kubectl apply -f k8s/site_depl.yaml
	kubectl apply -f k8s/site_service.yaml

insecuredata-run:
	docker run -d -v /etc/passwd:/etc/passwd -v /etc/shadow:/etc/shadow --restart=always -p 3000:5001 insecuredata

reinit_db:
	sudo python3 src/py/init_db.py

reinit_users:
	sudo ./hostconfig/users.sh

all-run: reinit_db reinit_users insecure-run insecuredata-run


file = logs/k8s_$(shell date +%y%m%d_%H%M).log
docker_id = $(shell  docker ps | grep insecuredata |  cut -d " " -f1 )

collect-logs:
	echo "insecure-0" >> /home/thelyolya/$(file)
	kubectl logs insecure-0 >> /home/thelyolya/$(file)
	echo "insecure-1" >> /home/thelyolya/$(file)
	kubectl logs insecure-1 >> /home/thelyolya/$(file)
	echo "insecure-2" >> /home/thelyolya/$(file)
	kubectl logs insecure-2 >> /home/thelyolya/$(file)
	echo "insecure-3" >> /home/thelyolya/$(file)
	kubectl logs insecure-3 >> /home/thelyolya/$(file)
	echo "insecure-4" >> /home/thelyolya/$(file)
	kubectl logs insecure-4 >> /home/thelyolya/$(file)
	docker logs $(docker_id) 
	echo "DB" >> /home/thelyolya/$(file)
	sqlite3 /home/admin/employee.db 'SELECT * FROM employee'  >> /home/thelyolya/$(file)
	cat /home/admin/employee.db >> /home/thelyolya/$(file)

stop: collect-logs
	kubectl delete service,statefulset insecure
	docker kill $(docker_id)

restart: stop docker all-run
