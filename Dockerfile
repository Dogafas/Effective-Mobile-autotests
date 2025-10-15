# Базовый образ с Python 3.10
FROM python:3.10-slim

# Установим переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Установим зависимости для Playwright
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    git \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Скопируем зависимости
COPY requirements.txt .

# Установим Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Установим Playwright и браузеры
RUN pip install playwright pytest pytest-playwright allure-pytest && \
    playwright install chromium

# Скопируем проект
COPY . .

# Команда по умолчанию (запуск тестов)
CMD ["pytest", "--alluredir=allure-results"]
