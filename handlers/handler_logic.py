# Файл с хендлерами кнопки "заказать разработку"
from aiogram import F, types, Router
# Импорты 2 штуки из файла handler_logic.py
# from kbds.inline import platform_kb
from text_message.text import business_card_text, questionnaire_text, commodity_text, webinar_text, other_text
from filters.chat_types import ChatTypeFilter
from text_message import text

from kbds import reply


# Помещаем этот файл в переменную для возможности импорта в основной файл.
handler_logic_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
handler_logic_router.message.filter(ChatTypeFilter(["private"]))


@handler_logic_router.message(F.text.casefold() == "заказать разработку бота")
async def about_cmd(message: types.Message):
    await message.answer(text.selling_text, reply_markup=reply.reply_markup)


# ______________________Начало второго меню_______________________
@handler_logic_router.message(F.text.casefold() == "telegram")
async def handle_telegram(message: types.Message):
    await message.answer(text.selling_text_2, reply_markup=reply.reply_markup_2)


@handler_logic_router.message(F.text.casefold() == "instagram")
async def handle_instagram(message: types.Message):
    await message.answer(text.selling_text_5, reply_markup=reply.reply_markup_2)


@handler_logic_router.message(F.text.casefold() == "вконтакте")
async def handle_vk(message: types.Message):
    await message.answer(text.selling_text_5, reply_markup=reply.reply_markup_2)


@handler_logic_router.message(F.text.casefold() == "whatsapp")
async def handle_whatsapp(message: types.Message):
    await message.answer(text.selling_text_5, reply_markup=reply.reply_markup_2)


@handler_logic_router.message(F.text.casefold() == "другое")
async def handle_other(message: types.Message):
    await message.answer(text.selling_text_2)
    await message.answer('Введите свои пожелания в поле ввода сообщений', reply_markup=reply.reply_markup_2)


# ________________________Начало 3 меню_______________________
@handler_logic_router.message(F.text.casefold() == "чат-бот визитка")
async def handle_business_card(message: types.Message):
    await message.answer(business_card_text, reply_markup=reply.back_selection)


@handler_logic_router.message(F.text.casefold() == "квиз-ботэто - опросник")
async def handle_questionnaire(message: types.Message):
    await message.answer(questionnaire_text, reply_markup=reply.back_selection)


@handler_logic_router.message(F.text.casefold() == "товарный бот - бот каталог")
async def handle_commodity(message: types.Message):
    await message.answer(commodity_text, reply_markup=reply.back_selection)


@handler_logic_router.message(F.text.casefold() == "автовебинарный бот")
async def handle_webinar_text(message: types.Message):
    await message.answer(webinar_text, reply_markup=reply.back_selection)


@handler_logic_router.message(F.text.casefold() == "другие услуги")
async def handle_other_2(message: types.Message):
    await message.answer(other_text, reply_markup=reply.back_selection)
# ___________________________________________________________

# # callback-хендлеры. Обработка логики inlain кнопок.
# from aiogram import F, types, Router
# from text_message.text import selling_text_2


# from filters.chat_types import ChatTypeFilter
# # Импортируем клавиатуру из inline.py
# from kbds.inline import platform_kb


# # Помещаем этот файл в переменную для возможности импорта в основной файл.
# handler_logic_router = Router()
# # Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# # используется только в чатах. Если gropup то в группах или оба сразу.
# handler_logic_router.message.filter(ChatTypeFilter(["private"]))

# # Хранилище данных пользователей
# order_data = {}


# # Функция для сохранения данных пользователя
# def save_user_data(user_id, user_text):
#     order_data[user_id] = {"platform": "", "user_text": user_text}


# # Фильтр: проверяем, начинается ли сообщение с "выбрать платформу"
# @handler_logic_router.message(F.text.func(lambda text: text.lower().startswith("выбрать платформу")))
# async def show_platform_buttons(message: types.Message):
#     await message.answer("Выберите платформу:", reply_markup=platform_kb)


# # 1️⃣ Декоратор для callback-хендлеров → @user_private_router.callback_query
# @handler_logic_router.callback_query()
# async def handle_telegram_callback(callback: types.CallbackQuery):
#     print("Кнопка нажата!")
#     if callback.data == "platform_instagram":
#         if callback.message:
#             await callback.message.answer(selling_text_2)
#         else:
#             await callback.answer("Сообщение недоступно")


# @handler_logic_router.callback_query()
# async def debug_callback(callback: types.CallbackQuery):
#     print(f"Получен callback: {callback.data}")
#     await callback.answer("Callback получен!")


# @handler_logic_router.callback_query(F.data == "platform_instagram")
# async def handle_instagram_callback(callback: types.CallbackQuery):
#     if callback.message:
#         await callback.message.answer(selling_text_2)
#     else:
#         await callback.answer("Сообщение недоступно")


# @handler_logic_router.callback_query(F.data == "platform_vk")
# async def handle_vk_callback(callback: types.CallbackQuery):
#     if callback.message:
#         await callback.message.answer(selling_text_2)
#     else:
#         await callback.answer("Сообщение недоступно")


# @handler_logic_router.callback_query(F.data == "platform_whatsapp")
# async def handle_Whatsapp_callback(callback: types.CallbackQuery):
#     if callback.message:
#         await callback.message.answer(selling_text_2)
#     else:
#         await callback.answer("Сообщение недоступно")


# @handler_logic_router.callback_query(F.data == "platform_other")
# async def handle_other_callback(callback: types.CallbackQuery):
#     if callback.message:
#         await callback.message.answer(selling_text_2)
#     else:
#         await callback.answer("Сообщение недоступно")


# @handler_logic_router.message(F.text)
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


# # from aiogram import F, Router, types


# # from filters.chat_types import ChatTypeFilter
# # from kbds.inline_1 import platform_kb

# # handler_logic_router = Router()

# # # Используем кастомный фильтр для групп и супергрупп
# # handler_logic_router.message.filter(ChatTypeFilter(['private']))


# # @handler_logic_router.message(F.text == 'Инлайн меню')  # Исправленный фильтр
# # async def show_inline_menu(message: types.Message):
# #     await message.answer('Инлайн кнопки ниже', reply_markup=platform_kb)


# # # Хендлер для обработки нажатия на кнопку "Алёрт"
# # @handler_logic_router.callback_query(lambda c: c.data == "show_alert")
# # async def alert_handler(callback: types.CallbackQuery):
# #     await callback.answer("Это всплывающее сообщение!", show_alert=True)


# # from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# # platform_kb = ReplyKeyboardMarkup(
# #     keyboard=[
# #         [
# #             KeyboardButton(text)
# #         ]
# #     ]
# # )
