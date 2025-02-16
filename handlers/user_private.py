from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import FSInputFile
from text_message import text
# Импорт Bold для того что бы сделать шрифт жирным
from aiogram.utils.formatting import Bold
# Импорты 2 штуки из файла handler_logic.py
# from kbds.inline import platform_kb
from filters.chat_types import ChatTypeFilter

from kbds import reply


# Помещаем этот файл в переменную для возможности импорта в основной файл.
user_private_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(text.selling_text_4, reply_markup=reply.submenu_markup)


@user_private_router.message(or_f(Command("menu"), F.text.casefold() == "меню"))
async def menu_cmd(message: types.Message):
    photo = FSInputFile("images/start_image_2.webp")
    await message.answer_photo(photo, "Выберите пункт меню, ниже ▩🧐", reply_markup=reply.submenu_markup)


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
    await message.answer(text.selling_text, reply_markup=reply.back_markup)


@user_private_router.message(F.text.casefold() == "стоимость")
async def cost_cmd(message: types.Message):
    await message.answer(text.selling_text_3, reply_markup=reply.back_markup)


# __________________3 меню, с оформлением__________________
@user_private_router.message(F.text.casefold() == "назад")
async def handle_back_2(message: types.Message):
    await message.answer("Вы уже в главном меню", reply_markup=reply.submenu_markup)


# @user_private_router.callback_query(F.data.in_({
#     "platform_telegram",
#     "platform_instagram",
#     "platform_vk",
#     "platform_whatsapp",
#     "platform_other"
# }))
# async def handle_platform_callback(callback: types.CallbackQuery):
#     if callback.message:
#         await callback.message.answer(selling_text_2)
#     await callback.answer()


# # 1️⃣ Декоратор для callback-хендлеров → @user_private_router.callback_query
# @user_private_router.callback_query()
# async def handle_telegram_callback(callback: types.CallbackQuery):
#     print("Кнопка нажата!")
#     if callback.data == "platform_telegram":
#         if callback.message:
#             await callback.message.answer(selling_text_2)
#         else:
#             await callback.answer("Сообщение недоступно")


# @user_private_router.callback_query(F.data == "platform_instagram")
# async def handle_instagram_callback(callback: types.CallbackQuery):
#     if callback.message:
#         await callback.message.answer(selling_text_2)
#     else:
#         await callback.answer("Сообщение недоступно")


# @user_private_router.callback_query(F.data == "platform_vk")
# async def handle_vk_callback(callback: types.CallbackQuery):
#     if callback.message:
#         await callback.message.answer(selling_text_2)
#     else:
#         await callback.answer("Сообщение недоступно")


# @user_private_router.callback_query(F.data == "platform_whatsapp")
# async def handle_Whatsapp_callback(callback: types.CallbackQuery):
#     if callback.message:
#         await callback.message.answer(selling_text_2)
#     else:
#         await callback.answer("Сообщение недоступно")


# @user_private_router.callback_query(F.data == "platform_other")
# async def handle_other_callback(callback: types.CallbackQuery):
#     if callback.message:
#         await callback.message.answer(selling_text_2)
#     else:
#         await callback.answer("Сообщение недоступно")


# @user_private_router.message(F.text)
# async def handle_user_text(message: types.Message):
#     if message.from_user:  # Проверяем, что from_user не None
#         user_id = message.from_user.id  # Получаем ID пользователя
#         user_text = message.text  # Получаем текст, который пользователь ввел

#         # Сохраняем введенный текст в словарь
#     if user_id in order_data:
#         order_data[user_id]["user_text"] = user_text
#         await message.answer(f"Спасибо за ваш ответ! Мы получили: {user_text}")

#         # Очистка данных пользователя после обработки
#         del order_data[user_id]
#     else:
#         await message.answer("Ошибка. Попробуйте снова.")


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
