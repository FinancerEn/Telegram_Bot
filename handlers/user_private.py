from aiogram import F, Router
from aiogram.filters import CommandStart, Command, or_f
from handlers.inlain_logic import UserState
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, Message
from filters.chat_types import ChatTypeFilter

# Импорт Bold для того что бы сделать шрифт жирным
from aiogram.utils.formatting import Bold

# Кастомные
from text_message import text
from kbds import inline, reply


# Помещаем этот файл в переменную для возможности импорта в основной файл.
user_private_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(CommandStart())
async def start_cmd(message: Message):
    # Извлекаем имя пользователя
    user_name = message.from_user.first_name if message.from_user else "Вы"
    photo = FSInputFile("images/reply.webp")
    await message.answer(f"{user_name}👋 Добро пожаловать! Этот бот — ваш личный гид в мире автоматизации продаж.", reply_markup=reply.submenu_markup)
    await message.answer(text.selling_text_4, reply_markup=reply.submenu_markup)
    await message.answer_photo(photo)
    # Что бы подключать inline меню по команде /start раскоментировать код ниже.
    # await message.answer(
    #     "📌 Всё просто: изучаете — выбираете нужное решение — оформляете заказ! Выберите пункт меню ниже:",
    #     reply_markup=inline.inline_keyboard_main,
    # )


@user_private_router.message(or_f(Command("menu"), F.text.lower() == "варианты меню"))
async def menu_cmd(message: Message):
    photo = FSInputFile("images/start_image_2.webp")
    await message.answer_photo(
        photo,
        "Посмотрите какие бывают меню 🧐 И выберите любое для проверки",
        reply_markup=inline.inline_menu_options,
    )


@user_private_router.message(F.text.casefold() == "кейсы")
async def cases_other_reply(message: Message):
    await message.answer("Примеры кейсов", reply_markup=reply.back_markup)
    await message.answer(text.cases_text, reply_markup=inline.platform_cases_kb)


@user_private_router.message(F.text.casefold() == "отзывы")
async def reviews_reply(message: Message):
    texts = Bold("Отзывы наших клиентов 😊")  # Делаем текст жирным
    await message.answer(
        texts.as_html(), parse_mode="HTML", reply_markup=reply.back_markup
    )

    photo = FSInputFile("images/feedback_1.webp")
    photo_2 = FSInputFile("images/feedback_2.webp")
    photo_3 = FSInputFile("images/feedback_3.webp")
    await message.answer_photo(photo)
    await message.answer_photo(photo_2)
    await message.answer_photo(photo_3)


@user_private_router.message(F.text.casefold() == "оплата")
async def payment_cmd(message: Message):
    await message.answer(text.payment_options_text, reply_markup=reply.submenu_markup)


@user_private_router.message(F.text.casefold() == "какие бывают боты, стоимость")
async def cost_cmd(message: Message):
    texts = Bold("Выберите интересующего вас бота и узнайте стоимость")
    await message.answer(
        texts.as_html(), parse_mode="HTML",
        reply_markup=inline.platform_services_price_kb)


@user_private_router.message(F.text.casefold() == "заказать разработку бота")
async def about_cmd(message: Message, state: FSMContext):
    await state.set_state(UserState.platform)
    # await message.answer(text.selling_text, reply_markup=reply.reply_markup)
    await message.answer(text.selling_text_8, reply_markup=inline.platform_kb)


# __________________3 меню, с оформлением__________________
@user_private_router.message(F.text.casefold() == "назад")
async def handle_back_2(message: Message):
    await message.answer("Вы уже в главном меню", reply_markup=reply.submenu_markup)


# Кнопка назад на предыдущее состояние
@user_private_router.message(lambda message: message.text.lower() == "на шаг назад")
async def back_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state:
        # Получаем историю состояний
        state_data = await state.get_data()
        prev_state = state_data.get("prev_state")  # Проверяем, есть ли предыдущее состояние

        if prev_state:
            await state.set_state(prev_state)  # Возвращаемся в предыдущее состояние
            await message.answer("Вы вернулись назад.")
        else:
            await state.clear()  # Если предыдущего состояния нет, очищаем FSM
            await message.answer("Вы вышли в главное меню.", reply_markup=reply.submenu_markup)
    else:
        await message.answer("Вы уже в главном меню.", reply_markup=reply.submenu_markup)


# Отменить заказ
@user_private_router.message(F.text.casefold() == "❌ Отменить заказ")
async def exit_order_process(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Вы вышли из оформления заказа. Чем могу помочь?", reply_markup=reply.submenu_markup)

# # Генерируем ответ на определённые ключевые слова
# # @user_private_router.message(lambda message: message.content_type == types.ContentType.TEXT)
# # async def echo(message: Message):
# #     text = message.text

# #     if text:  # Проверяем, что text не None
# #         if text.lower() in ['привет', 'здравствуйте', 'добрый день', 'hi', 'hello', 'добрый вечер', 'доброе утро']:
# #             await message.answer('Здравствуйте!')
# #         elif text.lower() in ['до свидания', 'досвидания', 'пока', 'пакеда', 'прощайте']:
# #             await message.answer('До свидания')
# #         else:
# #             await message.answer(text)
# #     else:
# #         await message.answer("Сообщение не содержит текста.")
