# callback-хендлеры. Обработка логики inlain кнопок.
from aiogram import F, types, Router
from text_message.text import selling_text_2


from filters.chat_types import ChatTypeFilter
# Импортируем клавиатуру из inline.py
from kbds.inline import platform_kb


# Помещаем этот файл в переменную для возможности импорта в основной файл.
inlain_logic_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
inlain_logic_router.message.filter(ChatTypeFilter(["private"]))

# Хранилище данных пользователей
order_data = {}


# Функция для сохранения данных пользователя
def save_user_data(user_id, user_text):
    order_data[user_id] = {"platform": "", "user_text": user_text}


# Фильтр: проверяем, начинается ли сообщение с "выбрать платформу"
@inlain_logic_router.message(F.text.func(lambda text: text.lower().startswith("выбрать платформу")))
async def show_platform_buttons(message: types.Message):
    await message.answer("Выберите платформу:", reply_markup=platform_kb)


# 1️⃣ Декоратор для callback-хендлеров → @user_private_router.callback_query
@inlain_logic_router.callback_query(F.data.startswith("platform_"))
async def handle_platform_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    platform = callback.data.split("_")[1]  # Получаем платформу

    # Сохраняем выбор пользователя
    order_data[user_id] = {"platform": platform, "user_text": ""}

    print(f"Пользователь {user_id} выбрал платформу: {platform}")
    if callback.message:
        await callback.message.answer(selling_text_2)
    else:
        await callback.answer("Сообщение недоступно")


# Обработка сообщений пользователя
#  Что делает? Если пользователь отправил сообщение после выбора платформы, оно сохраняется в order_data[user_id]["user_text"].
# Бот подтверждает получение сообщения. После обработки данные удаляются.
@inlain_logic_router.message(F.text)
async def handle_user_text(message: types.Message):
    if message.from_user:  # Проверяем, что from_user не None
        user_id = message.from_user.id  # Получаем ID пользователя
        user_text = message.text  # Получаем текст, который пользователь ввел

        # Сохраняем введенный текст в словарь
        if user_id in order_data:
            order_data[user_id]["user_text"] = user_text
            await message.answer(f"Спасибо за ваш ответ! Мы получили: {user_text}")

            # Очистка данных пользователя после обработки
            del order_data[user_id]
        else:
            await message.answer("Ошибка. Попробуйте снова.")
