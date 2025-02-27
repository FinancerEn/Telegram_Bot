from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import FSInputFile
from text_message import text
from aiogram.types import CallbackQuery
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
async def start_cmd(message: types.Message):
    await message.answer(text.selling_text_4, reply_markup=reply.submenu_markup)


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


@user_private_router.callback_query(F.data == "inline_menu")
async def show_inline_menu(callback: CallbackQuery):
    await callback.message.answer(text.information_inline_menu, reply_markup=inline.platform_services_kb)
    await callback.answer()


@user_private_router.callback_query(F.data == "reply_menu")
async def show_reply_menu(callback: CallbackQuery):
    photo = FSInputFile("images/reply.webp")
    await callback.message.answer(text.information_reply_menu, reply_markup=reply.submenu_markup)
    await callback.message.answer_photo(photo)
    await callback.answer()


@user_private_router.callback_query(F.data == "standard_back")
async def show_reply_menu(callback: CallbackQuery):
    photo = FSInputFile("images/difolt_menu.webp")
    await callback.message.answer(text.information_difolt_menu)
    await callback.message.answer_photo(photo)
    await callback.answer()


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
