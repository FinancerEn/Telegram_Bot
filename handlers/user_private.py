from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import FSInputFile, CallbackQuery, Message
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
    photo = FSInputFile("images/reply.webp")
    await message.answer(text.selling_text_4, reply_markup=reply.submenu_markup)
    await message.answer_photo(photo)


@user_private_router.message(or_f(Command("menu"), F.text.lower() == "варианты меню"))
async def menu_cmd(message: types.Message):
    photo = FSInputFile("images/start_image_2.webp")
    await message.answer_photo(photo, "Посмотрет какие бывают меню 🧐 И выберите любое для проверки",
                               reply_markup=inline.inline_menu_options)


@user_private_router.message(F.text.casefold() == "отзывы")
async def reviews(message: types.Message):
    texts = Bold("Отзывы наших клиентов 😊")  # Делаем текст жирным
    await message.answer(texts.as_html(), parse_mode="HTML", reply_markup=reply.back_markup)

    photo = FSInputFile("images/review1.webp")
    photo_2 = FSInputFile("images/review1.webp")
    await message.answer_photo(photo)
    await message.answer_photo(photo_2)


@user_private_router.message(F.text.casefold() == "варианты оплаты")
async def payment_cmd(message: types.Message):
    await message.answer(text.selling_text, reply_markup=inline.platform_kb)


@user_private_router.message(F.text.casefold() == "стоимость")
async def cost_cmd(message: types.Message):
    await message.answer(text.selling_text_3, reply_markup=reply.back_markup)


# варианты меню
@user_private_router.callback_query(F.data == "inline_menu")
async def show_inline_menu(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.answer(text.information_inline_menu, reply_markup=inline.inline_options)
        await callback.answer()


# варианты меню
@user_private_router.callback_query(F.data == "reply_menu")
async def show_reply_menu(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        photo = FSInputFile("images/reply.webp")
        await callback.message.answer(text.information_reply_menu, reply_markup=reply.submenu_markup)
        await callback.message.answer_photo(photo)
        await callback.answer()


# варианты меню
@user_private_router.callback_query(F.data == "standard_back")
async def show_default_menu(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        photo = FSInputFile("images/difolt_menu.webp")
        await callback.message.answer(text.information_difolt_menu)
        await callback.message.answer_photo(photo)
        await callback.answer()


# варианты inline меню
# Хендлер с переходом(ссылкой) в телеграмм группу и демонстрации какие бывают ссылки.
@user_private_router.callback_query(F.data == "link_resource")
async def send_link(callback: CallbackQuery):
    if callback.message is None:
        await callback.answer("Ошибка: Не удалось обработать запрос.", show_alert=True)
        return

    group_link = "https://t.me/+DDiXtpAlb7AxZmIy"
    message_text = f"{text.sample_url_text}\n\n🔗 [Перейти в группу]({group_link})"

    await callback.message.answer(
        message_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=inline.inline_back_1  # Вот здесь теперь передаём клавиатуру
    )
    await callback.answer()  # Просто закрываем "часики"


# Варианты меню:
# Хендлер с демонстрацией каким может быть текст который открывается при нажатии на inline кнопку.
@user_private_router.callback_query(F.data == "text_button")
async def handle_sample_text(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.answer(text.sample_text, reply_markup=inline.inline_back_1)
        await callback.answer()


# Варианты меню. Пример картинки.
@user_private_router.callback_query(F.data == "image_button")
async def handle_sample_image(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        photo = FSInputFile("images/sample_image.webp")
        await callback.message.answer_photo(photo)
        await callback.message.answer(text.sample_image_text, reply_markup=inline.inline_back_1)
        await callback.answer()


# Варианты меню. Пример картинки.
@user_private_router.callback_query(F.data == "other_menu")
async def handle_sample_menu(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.answer("Посмотрет какие бывают меню 🧐 И выберите любое для проверки",
                                      reply_markup=inline.inline_menu_options)
        await callback.answer()


# __________________3 меню, с оформлением__________________
@user_private_router.message(F.text.casefold() == "назад")
async def handle_back_2(message: types.Message):
    await message.answer("Вы уже в главном меню", reply_markup=reply.submenu_markup)


# Варианты меню. Кнопка назад для демонстративного inline меню.
@user_private_router.callback_query(F.data == "back_to_menu")
async def handle_back_3(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer_photo(photo, "Посмотрет какие бывают меню 🧐 И выберите любое для проверки",
                                            reply_markup=inline.inline_menu_options)


@user_private_router.callback_query(F.data == "back_menu")
async def handle_back_4(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.answer(text.information_inline_menu, reply_markup=inline.inline_options)


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
