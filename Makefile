help:
## The following commands can be used:
	@sed -n 's/^##//p' ${MAKEFILE_LIST}

env-up:
	docker-compose up -d --build

env-down:
	docker-compose down

env-clear:
	docker-compose down --remove-orphans -v # --rmi=all

app:
	docker exec -it py_clickurl_app bash

env-roll-migration:
## env-roll-migration: from env roll all three migrations: user, url and init data
	docker exec -it py_clickurl_app make roll-migration

env-roll-back-migration:
## env-roll-back-migration:	from env roll back to base position
	docker exec -it py_clickurl_app make roll-back-migration

roll-migration:
## roll-migration:	roll all three migrations: user, url and init data
	alembic upgrade fe4e4fbeaa33

roll-back-migration:
## roll-back-migration:	roll back to base position
	alembic downgrade base

browse-todo-links:
	browse http://localhost:8080/todo-links
