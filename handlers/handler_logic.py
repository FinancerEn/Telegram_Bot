# Файл с хендлерами кнопки "заказать разработку"
# from aiogram import F, types, Router
# from text_message import text

# # Импорты 2 штуки из файла handler_logic.py
# # from kbds.inline import platform_kb
# # Раскоментировать что бы подключить реплай меню для логики оформления заказа
# from text_message.text import (
#     business_card_text,
#     questionnaire_text,
#     catalog_text,
#     webinar_text,
#     other_text,
#     selling_text_6,
# )

# from handlers.inlain_logic import UserState
# from aiogram.fsm.context import FSMContext
# from filters.chat_types import ChatTypeFilter
# from text_message import text

# from kbds import inline, reply


# Помещаем этот файл в переменную для возможности импорта в основной файл.
# handler_logic_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
# handler_logic_router.message.filter(ChatTypeFilter(["private"]))


# # ______________________Начало второго меню_______________________
# @handler_logic_router.message(F.text.casefold() == "telegram")
# async def handle_telegram(message: types.Message):
#     await message.answer(text.selling_text_2, reply_markup=reply.reply_markup_2)
#     await message.answer("Выбрать чат бота", reply_markup=inline.platform_services_kb)


# @handler_logic_router.message(F.text.casefold() == "instagram")
# async def handle_instagram(message: types.Message):
#     await message.answer(text.selling_text_2, reply_markup=reply.reply_markup_2)
#     await message.answer("Выбрать чат бота", reply_markup=inline.platform_services_kb)


# @handler_logic_router.message(F.text.casefold() == "вконтакте")
# async def handle_vk(message: types.Message):
#     await message.answer(text.selling_text_2, reply_markup=reply.reply_markup_2)
#     await message.answer("Выбрать чат бота", reply_markup=inline.platform_services_kb)


# @handler_logic_router.message(F.text.casefold() == "whatsapp")
# async def handle_whatsapp(message: types.Message):
#     await message.answer(text.selling_text_2, reply_markup=reply.reply_markup_2)
#     await message.answer("Выбрать чат бота", reply_markup=inline.platform_services_kb)


# @handler_logic_router.message(F.text.casefold() == "другое")
# async def handle_other(message: types.Message):
#     await message.answer(text.selling_text_2)
#     await message.answer(
#         "Введите свои пожелания в поле ввода сообщений",
#         reply_markup=reply.reply_markup_2,
#     )
#     await message.answer("Выбрать чат бота", reply_markup=inline.platform_services_kb)


# # ________________________Начало 3 меню_______________________
# @handler_logic_router.message(F.text.casefold() == "чат-бот визитка")
# async def handle_business_card(message: types.Message):
#     await message.answer(business_card_text, reply_markup=reply.back_selection)
#     await message.answer("Оформить заказ", reply_markup=inline.inline_back_selection)


# @handler_logic_router.message(F.text.casefold() == "квиз-ботэто - опросник")
# async def handle_questionnaire(message: types.Message):
#     await message.answer(questionnaire_text, reply_markup=reply.back_selection)
#     await message.answer("Оформить заказ", reply_markup=inline.inline_back_selection)


# @handler_logic_router.message(F.text.casefold() == "товарный бот - бот каталог")
# async def handle_commodity(message: types.Message):
#     await message.answer(catalog_text, reply_markup=reply.back_selection)
#     await message.answer("Оформить заказ", reply_markup=inline.inline_back_selection)


# @handler_logic_router.message(F.text.casefold() == "автовебинарный бот")
# async def handle_webinar_text(message: types.Message):
#     await message.answer(webinar_text, reply_markup=reply.back_selection)
#     await message.answer("Оформить заказ", reply_markup=inline.inline_back_selection)


# @handler_logic_router.message(F.text.casefold() == "другие услуги")
# async def handle_other_2(message: types.Message):
#     await message.answer(text.selling_text_2, reply_markup=reply.back_selection)
#     await message.answer("Или выыберите пункт меню ниже", reply_markup=inline.inline_back_selection)


# # __________________________________ 4 меню______________________________________
# @handler_logic_router.message(F.text.casefold() == "оформить заказ")
# async def decoration_other(message: types.Message):
#     await message.answer(selling_text_6, reply_markup=reply.last_markup)


# @handler_logic_router.message(F.text.casefold() == "назад к выбору платформы")
# async def handle_back(message: types.Message):
#     await message.answer(text.selling_text, reply_markup=reply.reply_markup)


# # __________________________________ 5 меню______________________________________
# @handler_logic_router.message(F.text.casefold() == "оформляем заказ")
# async def handle_sending_the_user(message: types.Message):
#     await message.answer("Вы уже в главном меню", reply_markup=reply.submenu_markup)
