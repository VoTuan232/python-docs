up:
	docker-compose up -d --build

exec:
	docker-compose exec python-locus-docs sh

run:
	docker-compose exec python-locus-docs sh -c "locust -f locustfile.py --worker --master-host master"
	