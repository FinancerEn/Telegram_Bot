from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import FSInputFile
from text_message import text
# Импорт Bold для того что бы сделать шрифт жирным
from aiogram.utils.formatting import Bold

from filters.chat_types import ChatTypeFilter

from kbds import reply, inline


# Помещаем этот файл в переменную для возможности импорта в основной файл.
user_private_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
user_private_router.message.filter(ChatTypeFilter(["private"]))


# dp.message - декоратор обработки событий приходящих к боту.
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    # reply_markup - обращаюсь к клавиатуре из файла reply.py, папки kbds.
    # Ответить с упоминанием автора код: await message.reply(message.text)
    await message.answer(text.selling_text_4, reply_markup=reply.submenu_kd)


#                          Хэндлеры:
@user_private_router.message(or_f(Command("menu"), F.text.casefold() == "меню"))
async def menu_cmd(message: types.Message):
    photo = FSInputFile("images/start_image_2.webp")
    await message.answer_photo(
        photo, "Что Вас интересует?🧐", reply_markup=reply.submenu_kd
    )


@user_private_router.message(F.text.casefold() == "отзывы")
async def reviews(message: types.Message):

    texts = Bold("Отзывы наших клиентов 😊")  # Делаем текст жирным
    await message.answer(texts.as_html(), parse_mode="HTML", reply_markup=reply.submenu_kd)

    photo = FSInputFile("images/review1.webp")
    photo_2 = FSInputFile("images/review1.webp")
    await message.answer_photo(photo)
    await message.answer_photo(photo_2)


@user_private_router.message(
    or_f(Command("Кейсы"), F.text.casefold() == "варианты оплаты")
)
async def payment_cmd(message: types.Message):
    await message.answer("Кейсы: Тут должны быть кейсы", reply_markup=reply.submenu_kd)


@user_private_router.message(F.text.casefold() == "заказать разработку бота")
async def about_cmd(message: types.Message):
    await message.answer(text.selling_text, reply_markup=inline.platform_kb)


@user_private_router.message(F.text.casefold() == "стоимость услуг")
async def new_menu_cmd(message: types.Message):
    await message.answer(text.selling_text_3, reply_markup=reply.submenu_kd)


# Генерируем ответ на определённые ключевые слова
# @user_private_router.message(lambda message: message.content_type == types.ContentType.TEXT)
# async def echo(message: types.Message):
#     text = message.text

#     if text:  # Проверяем, что text не None
#         if text.lower() in ['привет', 'здравствуйте', 'добрый день', 'hi', 'hello', 'добрый вечер', 'доброе утро']:
#             await message.answer('Здравствуйте!')
#         elif text.lower() in ['до свидания', 'досвидания', 'пока', 'пакеда', 'прощайте']:
#             await message.answer('До свидания')
#         else:
#             await message.answer(text)
#     else:
#         await message.answer("Сообщение не содержит текста.")
