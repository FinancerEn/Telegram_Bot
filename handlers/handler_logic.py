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
