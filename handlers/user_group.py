# Удаляем сообщения если они содержат ругательные слова:
from string import punctuation
from aiogram import Bot, types, Router
import aiogram
from aiogram.filters import Command
from telegram import ChatMemberAdministrator, ChatMemberOwner
# Список запрещённых слов
from swearing.exception import restricted_words
from filters.chat_types import ChatTypeFilter


user_group_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


@user_group_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id

    try:
        admins_list = await bot.get_chat_administrators(chat_id)
    except aiogram.exceptions.TelegramBadRequest:
        admins_list = []  # Если ошибка, список пустой

    # Фильтруем владельца и администраторов, сразу проверяя user
    admin_ids = [
        admin.user.id for admin in admins_list
        if isinstance(admin, (ChatMemberOwner, ChatMemberAdministrator)) and admin.user is not None
    ]

    setattr(bot, "my_admins_list", admin_ids)  # Сохраняем ID админов в атрибут бота

    # Проверяем, есть ли вообще пользователь в сообщении перед удалением
    if message.from_user and message.from_user.id in admin_ids:
        try:
            await message.delete()
        except aiogram.exceptions.TelegramForbidden:
            pass  # У бота может не быть прав на удаление сообщений


# Функция для очистки текста от пунктуации
def clean_text(text: str) -> str:
    return text.translate(str.maketrans('', '', punctuation))


# Обработка только текстовых сообщений
@user_group_router.message(lambda message: message.text)
async def cleaner(message: types.Message):
    # Проверка, что текст сообщения и имя пользователя существуют
    if message.text is None or message.from_user is None:
        return

    # Очистка текста от пунктуации и приведение к нижнему регистру
    cleaned_text = clean_text(message.text).lower()

    # Проверка на наличие запрещённых слов
    if any(word in cleaned_text.split() for word in restricted_words):
        # Если имя пустое, подставить "Участник"
        user_name = message.from_user.first_name or "Участник"  # Если имя пустое, подставить "Участник"
        await message.answer(f"{user_name}, соблюдайте порядок в чате")
        await message.delete()
        # Закомментированный код, он банит пользователя который использовал слова
        # await message.chat.ban(message.from_user.id)
