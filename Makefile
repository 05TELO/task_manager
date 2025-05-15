.PHONY: help build down up deploy test cov lint makemigrations migrate

all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help: # Show help for each of the Makefile recipes.
	@grep -E "^[a-zA-Z0-9 -]+:.*#"  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done


build: # Build docker images
	docker compose -f docker/compose.yml --project-directory . build
	
up: # Start docker containers
	docker compose -f docker/compose.yml --project-directory . up --remove-orphans -d

db: # Start db
	docker compose -f docker/compose.yml --project-directory . up db --remove-orphans -d

down: # Stop docker containers
	docker compose -f docker/compose.yml --project-directory . down --remove-orphans

prune: # Stop docker containers
	docker compose -f docker/compose.yml --project-directory . down --remove-orphans -v

collectstatic: # Make migrations
	docker compose -f docker/compose.yml --project-directory . exec api python manage.py collectstatic --noinput

makemigrations: # Make migrations
	docker compose -f docker/compose.yml --project-directory . exec api python manage.py makemigrations

migrate: # Migrate database
	docker compose -f docker/compose.yml --project-directory . exec api python manage.py migrate

test: # Run tests
	docker compose -f docker/compose.yml --project-directory . run --rm api pytest .

.PHONY: create-tasks

create-tasks:
	@echo "Creating tasks for Telegram User ID: $(TELEGRAM_USER_ID)"
	docker compose -f docker/compose.yml --project-directory . run --rm api python manage.py create_tasks $(TELEGRAM_USER_ID)