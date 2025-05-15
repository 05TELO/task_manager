# Task manager

Простое веб-приложение для постановки и отслеживания задач с уведомлениями в Telegram через бота.

Приложение разворачивается с помощью **Docker Compose**.

---

## 🧱 Требования

Для запуска приложения вам понадобится установленный:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [make](https://ru.wikipedia.org/wiki/Make)

---

## 📦 Установка и запуск

### 1. Склонируйте репозиторий:
```bash
git clone git@github.com:05TELO/leaf33.git
cd leaf33
```

### 2. Создайте `.env` файл:
Создайте файл `.env` в корне проекта, основываясь на примере:

```bash
cp .env.example .env
```

Откройте файл `.env` и укажите актуальные данные для подключения к БД, Django и т.п.

---

## 🔧 Запуск приложения

Выполните команду:

```bash
make build && make up
```

---

## 🧪 Запуск тестов

Выполните команду:

```bash
docker compose run --remove-orphans app pytest .
```

---

## 🌐 Функционал приложения

- **[http://localhost:80](http://localhost:80)** — документация API.


---

## 🛑 Остановка приложения

Чтобы остановить работу сервисов:

```bash
make down
```
