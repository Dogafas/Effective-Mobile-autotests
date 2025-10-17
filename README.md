# Effective Mobile Autotests

Автотесты для сайта effective-mobile.ru с использованием Playwright и pytest.

## Быстрый старт

### Универсальный способ (все ОС):
```bash
# Linux/macOS:
./run-tests.sh

# Windows:
run-tests.bat

# Или через Docker Compose:
docker-compose run --rm tests
docker-compose up -d allure
```

### Через Makefile (Linux/macOS):
```bash
make help               # Показать все доступные команды
make docker-build       # Собрать Docker образ
make docker-check-all   # Запустить все проверки
make docker-run         # Запустить тесты с отчетом
```

## Команды Docker

### Основные команды
- `make docker-build` - Собрать Docker образ
- `make docker-format` - Форматировать код (black + isort)
- `make docker-lint` - Проверить код линтером (flake8 + mypy)
- `make docker-test` - Запустить тесты
- `make docker-check-all` - Запустить все проверки

### Управление контейнером
- `make docker-run` - Запустить тесты с отчетом Allure
- `make docker-stop` - Остановить контейнер
- `make docker-restart` - Перезапустить контейнер

### Отчеты
- `make allure-report` - Сгенерировать отчет Allure
- `make allure-stop` - Остановить Allure сервис

### Утилиты
- `make clean` - Очистить временные файлы
- `make help` - Показать справку

## Просмотр отчета

После выполнения тестов:

```bash
make docker-run         # Запустить тесты
make allure-report      # Открыть отчет Allure
```

Отчет будет доступен по адресу: http://localhost:4040/allure-docker-service/projects/default/reports/latest/index.html

Для остановки сервиса: `make allure-stop`

## Структура проекта

- `pages/` - Page Object классы
- `tests/` - Тестовые сценарии
- `conftest.py` - Конфигурация pytest
- `requirements.txt` - Зависимости Python
- `Makefile` - Команды для разработки
- `Dockerfile` - Конфигурация Docker
- `pytest.ini` - Настройки pytest
- `pyproject.toml` - Конфигурация проекта
- `.flake8` - Настройки линтера
- `docker-compose.yml` - Конфигурация Docker Compose
- `run-tests.sh` - Скрипт для Linux/macOS
- `run-tests.bat` - Скрипт для Windows

## Совместимость с ОС

Проект работает на всех операционных системах:

- **Linux** - полная поддержка всех команд
- **macOS** - полная поддержка всех команд
- **Windows** - используйте `run-tests.bat` или Docker Compose

**Требования:** Docker и Docker Compose