# Импорты Питона.
import asyncio
import os

# Импорты фреймворка.
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import load_dotenv

# Подключаем наш кастомный файл взаимодействия с пользователем.
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from handlers.admin_private import admin_router

# from handlers.handler_logic import handler_logic_router


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
dp.include_router(user_group_router)
dp.include_router(admin_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    # Удаляем сохранённое меню команд
    await bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

    # Настройка команд, которые видно при нажатии на "/" в чате с ботом.
    # private — это список команд, который в
    # bot.set_my_commands: Устанавливает список доступных команд для бота.
    # scope=BotCommandScopeAllPrivateChats: Область действия команд.
    # В данном случае команды будут видны только в приватных чатах с ботом (не в группах или каналах).

    # Если потребуется обратно установить меню, раскомментировать код ниже:
    # try:
    #     await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    # except Exception as e:
    #     print(f"Ошибка: {e}")
    # await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == "__main__":
    asyncio.run(main())
