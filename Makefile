run-db:
	docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_DB=postgres -d postgres