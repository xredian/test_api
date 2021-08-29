run-db:
	docker run --name test_api -p 5432:5432 -e POSTGRES_PASSWORD=root -e POSTGRES_DB=test_api -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres
