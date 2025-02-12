# Фильтруем события по группам, чатам отдельно.
# Импортируем Filter базовый класс.
import aiogram
from aiogram.filters import Filter
from aiogram.types import Message
from aiogram import Bot, types
from telegram import ChatMemberAdministrator, ChatMemberOwner


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __call__(self, message: Message) -> bool:
        return message.chat.type in self.chat_types


class IsAdmin(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: types.Message, bot: Bot) -> bool:
        if not message.from_user:  # Проверяем, есть ли вообще пользователь
            return False

        chat_id = message.chat.id  # ID чата (группы)
        try:
            admins = await bot.get_chat_administrators(chat_id)
        except aiogram.exceptions.TelegramBadRequest:
            admins = []
        # Фильтруем только владельца и администраторов
        admins = [
            member for member in admins
            if isinstance(member, (ChatMemberOwner, ChatMemberAdministrator)) and member.user is not None
        ]

        admin_ids = [admin.user.id for admin in admins]  # Достаем их ID

        return message.from_user.id in admin_ids
