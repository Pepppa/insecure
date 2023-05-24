.PHONY: docker-insecure docker-insecuredata insecure-run insecuredata-run reinit-db collect-logs restart

all: docker all-run

k8s ?= off
hostviolations ?= off

docker-insecure:
	docker build . -f docker/site/Dockerfile -t insecuremain --network=host

docker-insecuredata:
	docker build . -f docker/secure/Dockerfile -t insecuredata --network=host

docker: docker-insecure docker-insecuredata

insecure-run:
ifeq ($(k8s),on)
	kubectl apply -f k8s/site_depl.yaml
	kubectl apply -f k8s/site_service.yaml
else
	docker run -d -v /etc/passwd:/etc/passwd -v /etc/shadow:/etc/shadow -v /home/admin:/home/admin --restart=always -p 5000:5000 insecuremain
endif

	

insecuredata-run:
	docker run -d -v /etc/passwd:/etc/passwd -v /etc/shadow:/etc/shadow --restart=always -p 3000:5001 insecuredata

reinit_db:
	sudo python3 src/py/init_db.py

reinit_users:
ifeq ($(hostviolations),on)
	sudo ./hostconfig/users.sh
else
	@echo "No host setup"
endif

all-run: reinit_db reinit_users insecure-run insecuredata-run


logdir ?= $(HOME)/logs
file = $(logdir)/k8s_$(shell date +%y%m%d_%H%M).log
docker_id_pass = $(shell  docker ps | grep -w insecuredata |  cut -d " " -f1 )
docker_id_main = $(shell  docker ps | grep -w insecuremain |  cut -d " " -f1 )


collect-logs:
	(mkdir -p $(logdir) )
	(if [ -z /home/admin/employee.db ] ; then \
	sqlite3 /home/admin/employee.db 'SELECT * FROM employee'  >> $(file) ;\
	cat /home/admin/employee.db >> $(file) ; \
	fi )

stop: collect-logs
ifeq ($(k8s),on)
	kubectl delete service,statefulset insecure
else
	@echo "insecuremain ID: $(docker_id_main)"
	docker kill $(docker_id_main)
endif
	@echo "insecuredata ID: $(docker_id_pass)"
	docker kill $(docker_id_pass)

restart: stop docker all-run
