build:
	@docker compose build


run:
	@docker compose up -d


stop:
	@docker compose stop


down:
	@docker compose down


restart:
	@docker compose down
	@docker compose up -d


%:
	@:
