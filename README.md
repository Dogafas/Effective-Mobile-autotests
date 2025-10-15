# Effective Mobile Autotests

Автотесты для сайта effective-mobile.ru с использованием Playwright и pytest.

## Быстрый старт

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

### Утилиты
- `make clean` - Очистить временные файлы
- `make help` - Показать справку

## Структура проекта

- `pages/` - Page Object классы
- `tests/` - Тестовые сценарии
- `utils/` - Вспомогательные утилиты
- `conftest.py` - Конфигурация pytest
- `requirements.txt` - Зависимости Python
- `Makefile` - Команды для разработки