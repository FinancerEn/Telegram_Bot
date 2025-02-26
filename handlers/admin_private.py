import os
from typing import Optional
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from database.models import Product
from filters.chat_types import ChatTypeFilter
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union

from kbds import reply

# Загружаем переменные окружения
load_dotenv()

# Получаем ID админа
ADMIN_ID_ENV = os.getenv("ADMIN_ID")
ADMIN_ID: Optional[int] = int(ADMIN_ID_ENV) if ADMIN_ID_ENV and ADMIN_ID_ENV.isdigit() else None


# Фильтр проверки администратора
class IsAdmin:
    async def __call__(self, message: Union[types.Message, None]) -> bool:
        if message is None or message.from_user is None:
            # print(f"🔍 Проверка IsAdmin: {message.from_user.id} -> {is_admin}")
            return False  # Если сообщения нет или оно анонимное — не админ

        return message.from_user.id == ADMIN_ID


# Маршрутизатор для администратора
admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())


class AddProduct(StatesGroup):
    # Шаги состояний
    name = State()
    description = State()
    price = State()
    image = State()

    product_for_change = None

    texts = {
        "AddProduct:name": "Введите название заново:",
        "AddProduct:description": "Введите описание заново:",
        "AddProduct:price": "Введите стоимость заново:",
        "AddProduct:image": "Этот стейт последний, поэтому...",
    }


# Состояния FSM для обработки заявок
class OrderState(StatesGroup):
    name = State()
    description = State()
    price = State()
    contact_info = State()


# Команда /admin для входа в режим администратора
@admin_router.message(Command("admin"), IsAdmin())
async def admin_panel(message: types.Message):
    await message.answer("Добро пожаловать в панель администратора!", reply_markup=reply.ADMIN_KB)


# Создание нового заказа
@admin_router.message(F.text == "Создать заказ")
async def create_order(message: types.Message, state: FSMContext):
    await message.answer("Введите имя клиента:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(OrderState.name)


# Хендлер отмены и сброса состояния должен быть всегда именно хдесь,
# после того как только встали в состояние номер 1 (элементарная очередность фильтров).
# Кнопка "Отмена" сбрасывает состояние FSM, то есть выводит пользователя из процесса создания заказа.
@admin_router.message(Command("отмена"), F.state)
@admin_router.message(F.text.casefold() == "отмена", F.state)
async def cancel_handler(message: types.Message, state: FSMContext):
    print(f"📌 Хэндлер 'Отмена' вызван. Текущее состояние: {await state.get_state()}")
    current_state = await state.get_state()
    if current_state is None:
        print("🔕 Состояние уже сброшено, выходим")
        return  # Уже сброшено, ничего не делаем
    print("🔴 Кнопка 'Отмена' нажата")  # Проверяем вызов
    await state.clear()  # Очищаем состояние
    await message.answer("Действия отменены ❌", reply_markup=reply.ADMIN_KB)


@admin_router.message(OrderState.name, F.text)
async def set_client_name(message: types.Message, state: FSMContext):
    await state.update_data(client_name=message.text)
    await message.answer("Опишите цель бота (например, автоматизация продаж):")
    await state.set_state(OrderState.description)


@admin_router.message(OrderState.description, F.text)
async def set_bot_purpose(message: types.Message, state: FSMContext):
    await state.update_data(bot_purpose=message.text)
    await message.answer("Укажите примерный бюджет клиента:")
    await state.set_state(OrderState.price)


@admin_router.message(OrderState.price, F.text)
async def set_budget(message: types.Message, state: FSMContext):
    await state.update_data(budget=message.text)
    await message.answer("Введите контактные данные клиента (номер телефона, Telegram):")
    await state.set_state(OrderState.contact_info)


@admin_router.message(OrderState.contact_info, F.text)
async def set_contact_info(message: types.Message, state: FSMContext, session: AsyncSession):
    data = await state.get_data()  # Получаем данные из FSM
    print(data)
    new_product = Product(
        name=data.get('client_name', 'Без названия'),  # У тебя было data['name'], но в FSM такого поля нет
        description=data.get('bot_purpose'),  # Уточняем правильные ключи
        price=float(data.get('budget', 0)),
        image=data.get("image", "default.jpg")
    )

    session.add(new_product)  # Добавляем в сессию
    await session.flush()
    await session.commit()  # Подтверждаем изменения

    await message.answer("Товар добавлен в базу!")


# Заглушки для просмотра и удаления заказов
@admin_router.message(F.text == "Просмотр заказов")
async def view_orders(message: types.Message):
    await message.answer("📋 Пока что заказов нет.")


@admin_router.message(F.text == "Удалить заказ")
async def delete_order(message: types.Message):
    await message.answer('🔍 Укажите ID заказа для удаления (пока не реализовано).')
