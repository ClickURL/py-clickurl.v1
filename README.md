# py-clickurl

## Deploy with docker compose

```shell
docker-compose up -d --build
```

## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED       STATUS       PORTS                              NAMES
894c987610a2   py-clickurl-app   "uvicorn main:app --…"   2 hours ago   Up 2 hours   0.0.0.0:8080->8000/tcp             py-clickurl-app-1       
3e08ac506e1b   postgres:15.2     "docker-entrypoint.s…"   2 hours ago   Up 2 hours   5433/tcp, 0.0.0.0:5433->5432/tcp   py-clickurl-postgresDB-1
```

## Migrations

After the application starts, navigate to `py-clickurl-app-1` container CLI
```
$ docker exec -t -i CONTAINER_ID /bin/bash
root@f2c828595531:/pu-clickurl_docker_container#
```
To make migrations using makefile

Get help about command which provides makefile
```
root@f2c828595531:/pu-clickurl_docker_container# make help
 The following commands can be used:
 roll-migration:        roll all three migrations: user, url and init data
 roll-back-migration:   roll back to base position
```
Roll migrations
```
root@f2c828595531:/pu-clickurl_docker_container# make roll-migration
alembic upgrade fe4e4fbeaa33
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> d8314c4d9cc2, users_table
INFO  [alembic.runtime.migration] Running upgrade d8314c4d9cc2 -> c87aaaac1243, url_table
INFO  [alembic.runtime.migration] Running upgrade c87aaaac1243 -> fe4e4fbeaa33, fixture_table
root@f2c828595531:/pu-clickurl_docker_container#
```
## Browser

After the application migration done, navigate to `http://localhost:8080` in your web browser and you should see the following `todo-links` page

## Stop docker

Stop and remove the containers
```
$ docker compose down
```