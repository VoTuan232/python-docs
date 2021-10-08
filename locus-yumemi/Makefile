up:
	docker-compose up -d --build

exec:
	docker-compose exec python-locus-yumemi sh

run:
	docker-compose exec python-locus-yumemi sh -c "locust -f locustfile.py --worker --master-host master --host=0.0.0.0"

	locust -f f1.py --worker --master-port=8001 --master-host master