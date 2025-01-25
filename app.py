# Импорты Питона.
import asyncio
import os
# Импорты фреймворка.
from aiogram import Bot, Dispatcher
# Импорты которые касаются проекта.
from dotenv import load_dotenv
from aiogram.types import BotCommandScopeAllPrivateChats
# Подключаем наш кастомный файл взаимодействия с пользователем.
from handlers.user_private import user_private_router
from common.bot_comds_list import private


load_dotenv()

# Указанны то что мы хотим что бы приходило из серверов телеграмма(те методы).
# Затем указываем эту нашу переменную ALLOWED_UPDATES в main, остальное приходить не будет.
ALLOWED_UPDATES = ['message', 'edited_message']

TOKEN = os.getenv('TOKEN')
if not TOKEN:
    raise ValueError("Переменная окружения 'TOKEN' не задана.")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Подключение маршрутов
dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # Настройка команд, которые видно при нажатии на "/" в чате с ботом.
    # private — это список команд, который в
    # bot.set_my_commands: Устанавливает список доступных команд для бота.
    # scope=BotCommandScopeAllPrivateChats: Область действия команд. В данном случае команды будут видны только в приватных чатах с ботом (не в группах или каналах).
    try:
        await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    except Exception as e:
        print(f"Ошибка: {e}")
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
