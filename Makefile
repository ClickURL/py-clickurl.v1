env-up:
	docker-compose up -d --build

env-down:
	docker-compose down

env-clear:
	docker-compose down --remove-orphans -v # --rmi=all

app:
	docker exec -it py_clickurl_app bash

roll-migration:
	docker exec -it py_clickurl_app make roll-migration

roll-back-migration:
	docker exec -it py_clickurl_app make roll-back-migration

browse-todo-links:
	browse http://localhost:8080/todo-links
