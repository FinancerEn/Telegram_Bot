import os
from typing import Optional
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from dotenv import load_dotenv
from database.models import Product
from filters.chat_types import ChatTypeFilter
from sqlalchemy.ext.asyncio import AsyncSession

# Загружаем переменные окружения
load_dotenv()

# Получаем ID админа
ADMIN_ID_ENV = os.getenv("ADMIN_ID")
ADMIN_ID: Optional[int] = int(ADMIN_ID_ENV) if ADMIN_ID_ENV and ADMIN_ID_ENV.isdigit() else None


# Фильтр проверки администратора
class IsAdmin:
    async def __call__(self, message: types.Message) -> bool:
        if message.from_user and message.from_user.id:
            is_admin = message.from_user.id == ADMIN_ID
            print(f"🔍 Проверка IsAdmin: {message.from_user.id} -> {is_admin}")  # Логируем
            return is_admin
        return False


# Маршрутизатор для администратора
admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())


# Клавиатура для администратора
ADMIN_KB = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Создать заказ")],
        [KeyboardButton(text="Просмотр заказов"), KeyboardButton(text="Удалить заказ")],
    ], resize_keyboard=True
)


# Состояния FSM для обработки заявок
class OrderState(StatesGroup):
    client_name = State()
    bot_purpose = State()
    budget = State()
    contact_info = State()


# Команда /admin для входа в режим администратора
@admin_router.message(Command("admin"), IsAdmin())
async def admin_panel(message: types.Message):
    await message.answer("Добро пожаловать в панель администратора!", reply_markup=ADMIN_KB)


# Создание нового заказа
@admin_router.message(F.text == "Создать заказ")
async def create_order(message: types.Message, state: FSMContext):
    await message.answer("Введите имя клиента:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(OrderState.client_name)


@admin_router.message(OrderState.client_name, F.text)
async def set_client_name(message: types.Message, state: FSMContext):
    await state.update_data(client_name=message.text)
    await message.answer("Опишите цель бота (например, автоматизация продаж):")
    await state.set_state(OrderState.bot_purpose)


@admin_router.message(OrderState.bot_purpose, F.text)
async def set_bot_purpose(message: types.Message, state: FSMContext):
    await state.update_data(bot_purpose=message.text)
    await message.answer("Укажите примерный бюджет клиента:")
    await state.set_state(OrderState.budget)


@admin_router.message(OrderState.budget, F.text)
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
    await message.answer("🔍 Укажите ID заказа для удаления (пока не реализовано).")
