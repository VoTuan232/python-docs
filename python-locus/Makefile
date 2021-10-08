up:
	docker-compose up -d --build

exec:
	docker-compose exec python-locus-docs sh

run:
	docker-compose exec python-locus-docs sh -c "locust -f locustfile.py --worker --master-host master"

run-server: 
	docker-compose exec python-locus-docs sh -c "node server/index.js"

run-master:
	docker-compose exec python-locus-docs sh -c "locust -f locustfile.py --master -H http://master:8089 && locust -f locustfile.py --worker --master-host master"
	