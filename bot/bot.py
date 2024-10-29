import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.filters import Command

API_TOKEN = '6885114225:AAHu4XrUgwGGmI9KVFkwWrmonE15zneoXtA'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()  # Используем хранилище в памяти
dp = Dispatcher(storage=storage)  # Передаем хранилище в диспетчер
router = Router()  # Создаем маршрутизатор


# Обработчик команды /start
@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Меня зовут Абзал. Я могу помочь вам для обработки данных о маркете. Отправь мне информацию, и я сохраню её.")


# Обработчик текстовых сообщений
@router.message()
async def handle_text(message: types.Message):
    # Получаем текст от пользователя
    text_data = message.text

    # Отправляем данные на сервер через POST запрос
    url = 'http://localhost:8000/markets/process-market-data/'  # Исправленный URL
    headers = {'Content-Type': 'text/plain'}  # Изменено на text/plain

    try:
        response = requests.post(url, headers=headers, data=text_data)  # Изменено на отправку текста напрямую
        if response.status_code == 200:
            await message.reply("Данные успешно отправлены и обработаны!")
        else:
            await message.reply(f"Ошибка на сервере: {response.status_code}")
    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}")


# Подключаем маршрутизатор к диспетчеру
dp.include_router(router)


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())