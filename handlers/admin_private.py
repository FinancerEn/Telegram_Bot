from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from filters.chat_types import ChatTypeFilter, IsAdmin


# Маршрутизатор для администратора
admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())


# Клавиатура для администратора
ADMIN_KB = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Создать заказ")],
        [KeyboardButton(text="Просмотр заказов"), KeyboardButton(text="Удалить заказ")],
    ],
    resize_keyboard=True,
    sizes=(2,),
)


# Состояния FSM для обработки заявок
class OrderState(StatesGroup):
    client_name = State()
    bot_purpose = State()
    budget = State()
    contact_info = State()


# Команда /admin для входа в режим администратора
@admin_router.message(Command("admin"))
async def admin_panel(message: types.Message):
    print("Всё работает отлично")
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
async def set_contact_info(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(
        f"✅ Новый заказ оформлен!\n\n"
        f"👤 Клиент: {data['client_name']}\n"
        f"📌 Цель бота: {data['bot_purpose']}\n"
        f"💰 Бюджет: {data['budget']}\n"
        f"📞 Контакты: {data['contact_info']}",
        reply_markup=ADMIN_KB
    )
    await state.clear()


# Заглушки для просмотра и удаления заказов
@admin_router.message(F.text == "Просмотр заказов")
async def view_orders(message: types.Message):
    await message.answer("📋 Пока что заказов нет.")


@admin_router.message(F.text == "Удалить заказ")
async def delete_order(message: types.Message):
    await message.answer("🔍 Укажите ID заказа для удаления (пока не реализовано).")
