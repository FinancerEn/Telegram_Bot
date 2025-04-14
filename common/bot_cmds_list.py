# Файл в котором описанна "Дефолтная кллавиатура" и все хендлеры связанные с ней.
from aiogram.types import BotCommand
from aiogram import types, Router
from aiogram.filters import Command
from handlers.inlain_logic import UserState
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from text_message import text

# Импорт Bold для того что бы сделать шрифт жирным
from aiogram.utils.formatting import Bold

# Импорты 2 штуки из файла handler_logic.py
# from kbds.inline import platform_kb
from filters.chat_types import ChatTypeFilter

from kbds import inline, reply


# Помещаем этот файл в переменную для возможности импорта в основной файл.
bot_cmds_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
bot_cmds_router.message.filter(ChatTypeFilter(["private"]))

private = [
    BotCommand(command="payment", description="Оплата"),
    BotCommand(command="cost", description="Какие бывают боты, стоимость"),
    BotCommand(command="reviews", description="Отзывы"),
    BotCommand(command="menu", description="Варианты меню"),
    BotCommand(command="kuysy", description="Кейсы"),
    BotCommand(command="order", description="Заказать разработку бота"),
]


@bot_cmds_router.message(Command("payment"))
async def payment_command(message: types.Message):
    await message.answer(text.payment_options_text, reply_markup=reply.submenu_markup)


@bot_cmds_router.message(Command("reviews"))
async def reviews_command(message: types.Message):
    photo = FSInputFile("images/feedback_1.webp")
    photo_2 = FSInputFile("images/feedback_2.webp")
    photo_3 = FSInputFile("images/feedback_3.webp")
    await message.answer_photo(photo)
    await message.answer_photo(photo_2)
    await message.answer_photo(photo_3)

    texts = Bold("Отзывы 😊")
    await message.answer(
        texts.as_html(), parse_mode="HTML", reply_markup=reply.submenu_markup
    )


@bot_cmds_router.message(Command("kuysy"))
async def kuysy_command(message: types.Message):
    await message.answer(text.payment_options_text, reply_markup=reply.submenu_markup)


@bot_cmds_router.message(Command("cost"))
async def order_command(message: types.Message):
    texts = Bold("Выберите интересующего вас бота и узнайте стоимость")
    await message.answer(
        texts.as_html(),
        parse_mode="HTML",
        reply_markup=inline.platform_services_price_kb,
    )


@bot_cmds_router.message(Command("order"))
async def cost_command(message: types.Message, state: FSMContext):
    await state.set_state(UserState.platform)
    # await message.answer(text.selling_text, reply_markup=reply.reply_markup)
    await message.answer(text.selling_text_8, reply_markup=inline.platform_kb)
