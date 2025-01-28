# Удаляем сообщения если они содержат ругательные слова:
from string import punctuation
from aiogram import types, Router

user_group_router = Router()

# Список запрещённых слов
restricted_words = {'говно', 'пидр', 'блядь', 'сука', 'пиздабол'}


# Функция для очистки текста от пунктуации
def clean_text(text: str) -> str:
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.message(lambda message: message.text)  # Обработка только текстовых сообщений
async def cleaner(message: types.Message):
    # Проверка, что текст сообщения и имя пользователя существуют
    if message.text is None or message.from_user is None:
        return

    # Очистка текста от пунктуации и приведение к нижнему регистру
    cleaned_text = clean_text(message.text).lower()

    # Проверка на наличие запрещённых слов
    if any(word in cleaned_text.split() for word in restricted_words):
        user_name = message.from_user.first_name or "Участник"  # Если имя пустое, подставить "Участник"
        await message.answer(f"{user_name}, соблюдайте порядок в чате")
        await message.delete()
        # Закомментированный код, он банит пользователя который использовал слова
        # await message.chat.ban(message.from_user.id)
