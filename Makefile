help:
## The following commands can be used:
	@sed -n 's/^##//p' ${MAKEFILE_LIST}

roll-migration:
## roll-migration:	roll all three migrations: user, url and init data
	cd backend && \
	alembic upgrade fe4e4fbeaa33

roll-back-migration:
## roll-back-migration:	roll back to base position
	cd backend && \
	alembic downgrade base
