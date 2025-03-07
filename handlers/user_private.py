from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import FSInputFile, Message
from text_message import text

# Импорт Bold для того что бы сделать шрифт жирным
from aiogram.utils.formatting import Bold

# Импорты 2 штуки из файла handler_logic.py
# from kbds.inline import platform_kb
from filters.chat_types import ChatTypeFilter

from kbds import inline, reply


# Помещаем этот файл в переменную для возможности импорта в основной файл.
user_private_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(CommandStart())
async def start_cmd(message: Message):
    # Извлекаем имя пользователя
    user_name = message.from_user.first_name if message.from_user else "Вы"
    photo = FSInputFile("images/reply.webp")
    await message.answer(f"{user_name}👋 Добро пожаловать! Этот бот — ваш личный гид в мире автоматизации продаж.", reply_markup=reply.submenu_markup)
    await message.answer(text.selling_text_4, reply_markup=reply.submenu_markup)
    await message.answer_photo(photo)
    # Что бы подключать inline меню по команде /start раскоментировать код ниже.
    # await message.answer(
    #     "📌 Всё просто: изучаете — выбираете нужное решение — оформляете заказ! Выберите пункт меню ниже:",
    #     reply_markup=inline.inline_keyboard_main,
    # )


@user_private_router.message(or_f(Command("menu"), F.text.lower() == "варианты меню"))
async def menu_cmd(message: types.Message):
    photo = FSInputFile("images/start_image_2.webp")
    await message.answer_photo(
        photo,
        "Посмотрите какие бывают меню 🧐 И выберите любое для проверки",
        reply_markup=inline.inline_menu_options,
    )


@user_private_router.message(F.text.casefold() == "отзывы")
async def reviews(message: types.Message):
    texts = Bold("Отзывы наших клиентов 😊")  # Делаем текст жирным
    await message.answer(
        texts.as_html(), parse_mode="HTML", reply_markup=reply.back_markup
    )

    photo = FSInputFile("images/review1.webp")
    photo_2 = FSInputFile("images/review1.webp")
    await message.answer_photo(photo)
    await message.answer_photo(photo_2)


@user_private_router.message(F.text.casefold() == "оплата и процесс работы")
async def payment_cmd(message: types.Message):
    await message.answer(text.payment_text_work, reply_markup=inline.inline_back_selection)


@user_private_router.message(F.text.casefold() == "стоимость")
async def cost_cmd(message: types.Message):
    await message.answer(text.selling_text_3, reply_markup=reply.back_markup)


# __________________3 меню, с оформлением__________________
@user_private_router.message(F.text.casefold() == "назад")
async def handle_back_2(message: types.Message):
    await message.answer("Вы уже в главном меню", reply_markup=reply.submenu_markup)


# # Генерируем ответ на определённые ключевые слова
# # @user_private_router.message(lambda message: message.content_type == types.ContentType.TEXT)
# # async def echo(message: types.Message):
# #     text = message.text

# #     if text:  # Проверяем, что text не None
# #         if text.lower() in ['привет', 'здравствуйте', 'добрый день', 'hi', 'hello', 'добрый вечер', 'доброе утро']:
# #             await message.answer('Здравствуйте!')
# #         elif text.lower() in ['до свидания', 'досвидания', 'пока', 'пакеда', 'прощайте']:
# #             await message.answer('До свидания')
# #         else:
# #             await message.answer(text)
# #     else:
# #         await message.answer("Сообщение не содержит текста.")
