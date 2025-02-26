# callback-хендлеры. Обработка логики inlain кнопок.
from aiogram import types, Router, F
from filters.chat_types import ChatTypeFilter
from kbds.inline import platform_kb, platform_services_kb, inline_back_selection


# Помещаем этот файл в переменную для возможности импорта в основной файл.
inlain_logic_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
inlain_logic_router.message.filter(ChatTypeFilter(["private"]))


# Хендлер для выбора платформы
@inlain_logic_router.callback_query(F.data.startswith("platform"))
async def handle_platform_callback(callback: types.CallbackQuery):
    if not callback.data:
        return

    platform_name = callback.data.split("_")[1]
    if isinstance(callback.message, types.Message):
        await callback.message.edit_text(
            f"Вы выбрали {platform_name.capitalize()}. Вот доступные услуги:",
            reply_markup=platform_services_kb,
        )
    await callback.answer()


@inlain_logic_router.callback_query(F.data.startswith("service_"))
async def handle_service_order(callback: types.CallbackQuery):
    if isinstance(callback.message, types.Message):
        await callback.message.edit_text(
            "Что хотите заказать?", reply_markup=inline_back_selection
        )
    await callback.answer()


# Хендлер для inline кнопки "Назад к выбору платформы"
@inlain_logic_router.callback_query(F.data == "back_to_platforms")
async def back_to_platforms(callback: types.CallbackQuery):
    if isinstance(callback.message, types.Message):  # Проверяем, доступно ли сообщение
        await callback.message.edit_text(
            "Выберите платформу:", reply_markup=platform_kb
        )
    await callback.answer()
