#!/bin/sh

# Создаём .env, если его нет
if [ ! -f /app/.env ]; then
    echo "BOT_TOKEN=${BOT_TOKEN}" > /app/.env
    echo ".env создан с BOT_TOKEN"
fi

exec python bot.py
