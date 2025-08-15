start:
	docker compose up --build -d

stop:
	docker compose down

restart:
	docker compose restart

status:
	docker compose ps

logs:
	docker compose logs -f
