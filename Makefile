compose-prod:
		docker-compose -f docker-compose.prod.yml up -d --build

compose-prod-down:
		docker-compose -f docker-compose.prod.yml down

compose:
		docker-compose -f docker-compose.yml up --build

compose-down:
		docker-compose -f docker-compose.yml down

test:
		pytest backend/tests
