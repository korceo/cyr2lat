# 1.Импорт библиотек
import os
from dotenv import load_dotenv

import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

from table import table # таблица для перевода

# 2. Инициализация объектов
# Для работы бота нужно создать файл .env и записать токен из BotFather в переменную BOT_TOKEN. Команда для консоли для удобства ↓↓↓
# echo "BOT_TOKEN=ваштокен" > .env

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(filename='bot.log',level=logging.INFO)


# 3. Обработка/Хэндлер на команду /start
@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name}, {user_id}: запустил бота.')
    await bot.send_message(chat_id=user_id, text=text)


# 4. Обработка/Хэндлер на любые сообщения
@dp.message()
async def fync(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    text = message.text
    converted = text.translate(table)
    logging.info(f'{user_name}, {user_id}: {text} →→→ {converted}.')
    await  message.answer(text=converted)


# 5. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)
