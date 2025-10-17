.PHONY: help docker-build docker-run docker-stop docker-restart docker-format docker-lint docker-test docker-check-all allure-report allure-stop clean

# Переменные
IMAGE_NAME = effective-mobile-tests
CONTAINER_NAME = effective-mobile-tests-container
DOCKER_RUN = docker run --rm -v $$(pwd):/app -w /app $(IMAGE_NAME)

help: ## Показать справку
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

docker-build: ## Собрать Docker образ
	docker build -t $(IMAGE_NAME) .

docker-format: docker-build ## Форматировать код в контейнере
	$(DOCKER_RUN) black pages/ tests/ conftest.py
	$(DOCKER_RUN) isort pages/ tests/ conftest.py

docker-lint: docker-build ## Проверить код линтером в контейнере
	$(DOCKER_RUN) flake8 pages/ tests/ conftest.py --max-line-length=88 --extend-ignore=E203,W503
	$(DOCKER_RUN) mypy pages/ tests/ conftest.py --ignore-missing-imports

docker-test: docker-build ## Запустить тесты в контейнере
	$(DOCKER_RUN) pytest

docker-check-all: docker-format docker-lint docker-test ## Запустить все проверки в контейнере

docker-run: docker-build ## Запустить тесты с отчетом
	docker run --name $(CONTAINER_NAME) --rm -v $$(pwd)/allure-results:/app/allure-results $(IMAGE_NAME)

docker-stop: ## Остановить контейнер
	docker stop $(CONTAINER_NAME) || true

docker-restart: docker-stop docker-run ## Перезапустить контейнер

allure-report: ## Сгенерировать отчет Allure
	docker stop allure-service || true
	docker run --rm -d --name allure-service -p 4040:5050 -e CHECK_RESULTS_EVERY_SECONDS=3 -e KEEP_HISTORY=1 -v $$(pwd)/allure-results:/app/allure-results frankescobar/allure-docker-service:latest
	@echo "Ожидание запуска сервиса..."
	@sleep 5
	@echo "Отчет доступен по адресу: http://localhost:4040/allure-docker-service/projects/default/reports/latest/index.html"
	@echo "Для остановки сервиса: make allure-stop"

allure-stop: ## Остановить Allure сервис
	docker stop allure-service || true

clean: ## Очистить временные файлы
	rm -rf allure-results/
	rm -rf allure-report/
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete