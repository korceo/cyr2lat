# Cyr2Lat Bot (МИД РФ 12.02.2020 № 2113) — запуск в Docker

Telegram-бот, который принимает ФИО на кириллице и возвращает транслитерацию на латиницу по приказу МИД РФ от 12.02.2020 № 2113.

## Требования

* Docker (Desktop/Engine) установлен и запущен
* Токен бота от BotFather

## Быстрый старт

### 1) Клонировать репозиторий

```bash
git clone https://github.com/<user>/<repo>.git
cd <repo>
```

### 2) Создать `.env` с токеном

```bash
echo 'BOT_TOKEN=123456:ABCDEF-your-token' > .env
```

### 3) Собрать образ

```bash
docker build -t cyr2lat .
```

### 4) Запустить контейнер

```bash
docker run -d --name cyr2lat-bot --env-file .env cyr2lat
```

### 5) Проверить логи

```bash
docker logs -f cyr2lat-bot
```

Готово — бот работает.

---

## Альтернатива: передать токен напрямую (без `.env`)

```bash
docker run -d --name cyr2lat-bot -e BOT_TOKEN="123456:ABCDEF-your-token" cyr2lat
```

---

