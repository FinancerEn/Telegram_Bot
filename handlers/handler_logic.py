# callback-хендлеры. Обработка логики inlain кнопок.
from aiogram import F, types, Router
from telegram import InlineKeyboardButton
from text_message import text


from filters.chat_types import ChatTypeFilter
# Импортируем клавиатуру из inline.py
from kbds.inline import platform_kb


# Помещаем этот файл в переменную для возможности импорта в основной файл.
user_private_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
user_private_router.message.filter(ChatTypeFilter(["private"]))


button_telegram = InlineKeyboardButton(text="Telegram", callback_data="platform_telegram")
button_instagram = InlineKeyboardButton(text="Instagram", callback_data="platform_instagram")


@user_private_router.message()
async def show_platform_buttons(message: types.Message):
    await message.answer("Выберите платформу:", reply_markup=platform_kb)


# 1️⃣ Декоратор для callback-хендлеров → @user_private_router.callback_query
@user_private_router.callback_query(F.data == "platform_telegram")
async def handle_telegram_callback(callback: types.CallbackQuery):
    if callback.message:
        await callback.message.answer(text.selling_text_2)
    else:
        await callback.answer("Сообщение недоступно")


@user_private_router.callback_query(F.data == "platform_instagram")
async def handle_instagram_callback(callback: types.CallbackQuery):
    if callback.message:
        await callback.message.answer(text.selling_text_2)
    else:
        await callback.answer("Сообщение недоступно")


@user_private_router.callback_query(F.data == "platform_Вконтакте")
async def handle_vk_callback(callback: types.CallbackQuery):
    if callback.message:
        await callback.message.answer(text.selling_text_2)
    else:
        await callback.answer("Сообщение недоступно")


@user_private_router.callback_query(F.data == "platform_Whatsapp")
async def handle_Whatsapp_callback(callback: types.CallbackQuery):
    if callback.message:
        await callback.message.answer(text.selling_text_2)
    else:
        await callback.answer("Сообщение недоступно")


@user_private_router.callback_query(F.data == "platform_Другое")
async def handle_other_callback(callback: types.CallbackQuery):
    if callback.message:
        await callback.message.answer(text.selling_text_2)
    else:
        await callback.answer("Сообщение недоступно")
