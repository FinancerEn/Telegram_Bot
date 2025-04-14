# callback-хендлеры. Обработка логики inlain кнопок.
import os
from typing import Optional
from aiogram import Router, F
from filters.chat_types import ChatTypeFilter
from aiogram.types import FSInputFile, CallbackQuery, Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# импорт для машины состояний
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Order

# импорт админа
from dotenv import load_dotenv

# Импорт Bold для того что бы сделать шрифт жирным
from aiogram.utils.formatting import Bold
from aiogram.utils.markdown import bold

# Кастомные импорты
from text_message import text
from kbds import inline, reply

load_dotenv()

GROUP_ID_ENV = os.getenv("GROUP_ID")
GROUP_ID: Optional[int] = (
    int(GROUP_ID_ENV) if GROUP_ID_ENV and GROUP_ID_ENV.isdigit() else None
)
# Помещаем этот файл в переменную для возможности импорта в основной файл.
inlain_logic_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если group то в группах или оба сразу.
inlain_logic_router.message.filter(ChatTypeFilter(["private"]))


class UserState(StatesGroup):
    platform = State()
    text_platform = State()
    bot_type = State()
    text_service = State()
    wishes = State()
    functional = State()
    name = State()
    contacts = State()


# _____________Хендлеры кнопки "заказать разработку бота"___________________
# Выбор платформы
# Это callback-хендлер, он ловит нажатие кнопок с callback_data, начинающимся на "platform_"
@inlain_logic_router.callback_query(F.data.startswith("platform"))
# callback: CallbackQuery — объект, содержащий информацию о нажатой кнопке.
# state: FSMContext — состояние пользователя (используется для сохранения данных между шагами).
async def handle_platform_callback(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    # Проверяет, что callback.data не пустое.
    if not callback.data:
        return

    # Разделяет callback_data="platform_telegram" по "_" и берёт "telegram"
    platform_name = callback.data.split("_")[1]

    # Если имя ещё не вводили, берём из Telegram first_name
    if isinstance(callback.message, Message):
        # Сохраняет platform_name в FSMContext, чтобы использовать позже.
        await state.update_data(platform=platform_name)
        # Переводит пользователя в состояние выбора типа бота.
        await state.set_state(UserState.bot_type)

    if isinstance(callback.message, Message):
        await callback.message.edit_text(
            f"Вы выбрали {platform_name.capitalize()}! Теперь выберите тип бота 🤖:",
            reply_markup=inline.platform_services_kb,
        )
        await callback.answer()


# Обработка ввода платформы (текст)
@inlain_logic_router.message(UserState.platform, F.text)
async def handle_platform_text(message: Message, state: FSMContext):
    platform_name = message.text.strip() if message.text else ""
    await state.update_data(platform=platform_name)
    await state.set_state(UserState.bot_type)

    await message.answer(
        f"Вы выбрали {platform_name.capitalize()}! Теперь выберите тип бота 🤖:",
        reply_markup=inline.platform_services_kb,
    )


# Обработка выбора типа бота (кнопка)
@inlain_logic_router.callback_query(F.data.startswith("service_"))
async def handle_service_order(callback: CallbackQuery, state: FSMContext):
    if not callback.data:
        return

    bot_type = callback.data.split("_")[1]
    if isinstance(callback.message, Message):
        await state.update_data(bot_type=bot_type)
        await state.set_state(UserState.wishes)

        await callback.message.edit_text(
            text.selling_text_7, reply_markup=inline.inline_back_selection_2
        )
        await callback.answer()


# Обработка ввода типа бота (текст)
@inlain_logic_router.message(UserState.bot_type, F.text)
async def handle_service_text(message: Message, state: FSMContext):
    bot_type = message.text.strip() if message.text else ""
    await state.update_data(bot_type=bot_type)
    await state.set_state(UserState.wishes)

    await message.answer(
        text.selling_text_7, reply_markup=inline.inline_back_selection_2
    )


# Обработка пожеланий (отправляет selling_text_9)
@inlain_logic_router.message(UserState.wishes, F.text)
async def handle_save_wishes(message: Message, state: FSMContext):
    await state.update_data(wishes=message.text)
    await state.set_state(UserState.functional)
    await message.answer(text.selling_text_9, reply_markup=inline.back_platform_1)


# Обработка функционала
@inlain_logic_router.message(UserState.functional, F.text)
async def handle_save_functional(message: Message, state: FSMContext):
    await state.update_data(functional=message.text)
    await state.set_state(UserState.name)
    await message.answer(
        "Отлично! Теперь введите ваше имя 📝:", reply_markup=inline.back_platform_1
    )


@inlain_logic_router.callback_query(F.data == "next_order")
async def handle_next_order(callback: CallbackQuery, state: FSMContext):
    texts = Bold("🔹 Записал! Теперь введите ваше имя 📝: 🔹")
    if isinstance(callback.message, Message):
        await state.set_state(UserState.name)
        await callback.message.edit_text(
            texts.as_html(), parse_mode="HTML", reply_markup=inline.back_platform_1
        )
        await callback.answer()


# Обработка имени
@inlain_logic_router.message(UserState.name, F.text)
async def handle_save_name(message: Message, state: FSMContext):
    text = (
        f"🔹 {bold('Спасибо')}, {bold(message.text)}! 🔹\n\n"
        "📞 Теперь укажите ваш номер телефона и удобный способ связи "
        "(Telegram, WhatsApp):"
    )

    await state.update_data(name=message.text)
    await state.set_state(UserState.contacts)
    await message.answer(text, parse_mode="HTML", reply_markup=inline.back_platform_1)


# Обработка контактов
@inlain_logic_router.message(UserState.contacts, F.text)
async def handle_save_contacts(message: Message, state: FSMContext):
    texts = Bold(
        "Отлично! Ваш заказ почти готов ✅. Нажмите 'Оформить заказ' для завершения! 🚀",
    )
    await state.update_data(contacts=message.text)
    await message.answer(
        texts.as_html(), parse_mode="HTML", reply_markup=inline.inline_back_selection
    )


# # Хендлер для кнокпи "другие услуги" при выборе бота
# @inlain_logic_router.callback_query(F.data.startswith("text_service_other"))
# async def handle_text_service_order(callback: CallbackQuery, state: FSMContext):
#     if not callback.data:
#         return

#     wishes = callback.data.split("_")[1]
#     if isinstance(callback.message, Message):
#         await state.update_data(bot_type=wishes)
#         await callback.message.edit_text(
#             text.selling_text_7, reply_markup=inline.inline_back_selection
#         )
#         await state.set_state(OrderState.wishes)
#         await callback.answer()


@inlain_logic_router.callback_query(F.data == "arrange_order")
async def confirm_order(
    callback: CallbackQuery, state: FSMContext, session: AsyncSession
):
    if isinstance(callback.message, Message):
        # Получаем все данные, которые пользователь вводил ранее
        data = await state.get_data()

        new_order = Order(
            user_id=callback.from_user.id,
            name=data.get("name"),
            platform=data.get("platform"),
            bot_type=data.get("bot_type"),
            wishes=data.get("wishes"),
            functional=data.get("functional"),
            contacts=data.get("contacts"),
        )

        session.add(new_order)
        # Сохраняем данные в БД
        await session.commit()

        # Формируем текст уведомления
        order_info = (
            f"🛒 *Новый заказ!*\n"
            f"👤 Имя: {data.get('name')}\n"
            f"💻 Платформа: {data.get('platform')}\n"
            f"🤖 Тип бота: {data.get('bot_type')}\n"
            f"📝 Пожелания: {data.get('wishes')}\n"
            f"📝 Функционал: {data.get('functional')}\n"
            f"📞 Контакты: {data.get('contacts')}\n"
            f"🔗 ID пользователя: {callback.from_user.id}"
        )
        # print(f"GROUP_ID_ENV = {GROUP_ID_ENV}")
        # Отправляем заказ в группу
        if GROUP_ID_ENV and callback.bot:
            await callback.bot.send_message(
                GROUP_ID_ENV, order_info, parse_mode="Markdown"
            )

        # Отправляем пользователю подтверждение
        await callback.message.edit_text(
            "✅ Ваш заказ успешно оформлен! Мы свяжемся с вами в ближайшее время."
        )

        # Очищаем состояние, так как заказ уже оформлен
        await state.clear()
        await callback.answer()


# _____________________________варианты меню_________________________________
@inlain_logic_router.callback_query(F.data == "inline_menu")
async def show_inline_menu(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.answer(
            text.information_inline_menu, reply_markup=inline.inline_options
        )
        await callback.answer()


# варианты меню
@inlain_logic_router.callback_query(F.data == "reply_menu")
async def show_reply_menu(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        photo = FSInputFile("images/reply.webp")
        await callback.message.answer(
            text.information_reply_menu, reply_markup=reply.submenu_markup
        )
        await callback.message.answer_photo(photo)
        await callback.message.answer(
            "Возвращаем вас обратно в выбор меню",
            reply_markup=inline.inline_menu_options,
        )
        await callback.answer()


# варианты меню
@inlain_logic_router.callback_query(F.data == "standard_back")
async def show_default_menu(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        photo = FSInputFile("images/difolt_menu.webp")
        await callback.message.answer(text.information_difolt_menu)
        await callback.message.answer_photo(photo)
        await callback.answer()


# варианты inline меню
# Хендлер с переходом(ссылкой) в телеграмм группу и демонстрации какие бывают ссылки.
@inlain_logic_router.callback_query(F.data == "link_resource")
async def send_link(callback: CallbackQuery):
    if callback.message is None:
        await callback.answer("Ошибка: Не удалось обработать запрос.", show_alert=True)
        return

    group_link = "https://t.me/+DDiXtpAlb7AxZmIy"
    message_text = f"{text.sample_url_text}"

    # Создаём inline-кнопку со ссылкой
    link_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Перейти в группу", url=group_link)],
            [InlineKeyboardButton(text="⬅ Назад к примерам", callback_data="back_menu")],
        ]
    )

    await callback.message.answer(
        message_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=link_button,  # Здесь передаём новую клавиатуру с кнопкой-ссылкой
    )
    await callback.answer()  # Закрываем "часики"


# Варианты меню:
# Хендлер с демонстрацией каким может быть текст который открывается при нажатии на inline кнопку.
@inlain_logic_router.callback_query(F.data == "text_button")
async def handle_sample_text(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.answer(
            text.sample_text, reply_markup=inline.inline_back_1
        )
        await callback.answer()


# Варианты меню. Пример картинки.
@inlain_logic_router.callback_query(F.data == "image_button")
async def handle_sample_image(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        photo = FSInputFile("images/sample_image.webp")
        await callback.message.answer_photo(photo)
        await callback.message.answer(
            text.sample_image_text, reply_markup=inline.inline_back_1
        )
        await callback.answer()


# # Варианты меню. Пример меню.
# @inlain_logic_router.callback_query(F.data == "other_menu")
# async def handle_sample_menu(callback: CallbackQuery):
#     if isinstance(callback.message, Message):
#         await callback.message.answer(
#             "Посмотрет какие бывают меню 🧐 И выберите любое для проверки",
#             reply_markup=inline.inline_menu_options,
#         )
#         await callback.answer()


# Кнопки НАЗАД
# Варианты меню. Кнопка назад для демонстративного inline меню.
@inlain_logic_router.callback_query(F.data == "back_to_menu")
async def handle_back_3(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer_photo(
            photo,
            "Посмотрет какие бывают меню 🧐 И выберите любое для проверки",
            reply_markup=inline.inline_menu_options,
        )


@inlain_logic_router.callback_query(F.data == "back_menu")
async def handle_back_4(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.answer(
            text.information_inline_menu, reply_markup=inline.inline_options
        )


@inlain_logic_router.callback_query(F.data == "back_main_price_inline")
async def handle_back_main_menu(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.answer(
            "📌 Вы уже в главном меню. Выберите пункт ниже:",
            reply_markup=inline.platform_services_price_kb,
        )


# inline меню для кнопки "Назад в главное меню"
# Работает так же для reply, дублирует её.
@inlain_logic_router.callback_query(F.data == "back_main_inlain")
async def back_to_main_inlain(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)  # Переводит состояние FSM в None
    await state.update_data({})  # Удаляет сохранённые данные FSM
    if isinstance(callback.message, Message):
        photo = FSInputFile("images/reply.webp")
        await callback.message.answer(
            text.selling_text_4, reply_markup=reply.submenu_markup
        )
        await callback.message.answer_photo(photo)
        await callback.answer()
        # # Редактируем inline-клавиатуру
        # await callback.message.edit_text(
        #     "📌 Всё просто: изучаете — выбираете нужное решение — оформляете заказ! Выберите пункт меню ниже",
        #     reply_markup=inline.inline_keyboard_main
        # )


@inlain_logic_router.callback_query(F.data == "cancel_order")
async def cancel_back_to_main_inlain(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)  # Переводит состояние FSM в None
    await state.update_data({})  # Удаляет сохранённые данные FSM
    if isinstance(callback.message, Message):
        photo = FSInputFile("images/reply.webp")
        await callback.message.answer(
            text.selling_text_4, reply_markup=reply.submenu_markup
        )
        await callback.message.answer_photo(photo)
        await callback.answer()


# Хендлер для inline кнопки "Назад к выбору платформы"
@inlain_logic_router.callback_query(F.data.in_(["arrange_back", "back_to_platforms"]))
async def back_to_platforms(callback: CallbackQuery):
    if isinstance(callback.message, Message):  # Проверяем, доступно ли сообщение
        await callback.message.edit_text(
            "Выберите платформу:", reply_markup=inline.platform_kb
        )
    await callback.answer()


@inlain_logic_router.callback_query(F.data == "cancel_order")
async def exit_order_process_inline(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(
        "Вы вышли из оформления заказа. Чем могу помочь?",
        reply_markup=reply.submenu_markup,
    )


@inlain_logic_router.callback_query(F.data == "back_list_bots")
async def back_list_bots_inline(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.answer("Примеры кейсов", reply_markup=reply.back_markup)
        await callback.message.answer(
            text.cases_text, reply_markup=inline.platform_cases_kb
        )


# # ____________________Обработка действий главного меню___________________________
# @inlain_logic_router.callback_query(F.data == "main_variants")
# async def inline_menu_options(callback: CallbackQuery):
#     if isinstance(callback.message, Message):
#         photo = FSInputFile("images/start_image_2.webp")
#         await callback.message.answer_photo(
#             photo,
#             "Посмотрите какие бывают меню 🧐 И выберите любое для проверки",
#             reply_markup=inline.inline_menu_options,
#         )


# # Обработка действий главного меню
# @inlain_logic_router.callback_query(F.data == "main_reviews")
# async def inline_main_menu_reviews(callback: CallbackQuery):
#     if isinstance(callback.message, Message):
#         photo = FSInputFile("images/review1.webp")
#         photo_2 = FSInputFile("images/review1.webp")
#         await callback.message.answer_photo(photo)
#         await callback.message.answer_photo(photo_2)
#         await callback.message.answer("🔹 Лучшие отзывы моих клиентов. 📌 Открываю главное меню",
#                                       reply_markup=inline.inline_keyboard_back_main_menu)


# # Обработка действий главного меню
# @inlain_logic_router.callback_query(F.data == "main_options")
# async def inline_main_menu_options_payment(callback: CallbackQuery):
#     if isinstance(callback.message, Message):
#         await callback.message.answer(text.selling_text, reply_markup=inline.inline_keyboard_back_main_menu)


# # Обработка действий главного меню
# @inlain_logic_router.callback_query(F.data == "main_cost_")
# async def inline_main_menu_cost(callback: CallbackQuery):
#     if isinstance(callback.message, Message):
#         await callback.message.answer(text.selling_text_3, reply_markup=inline.inline_keyboard_back_main_menu)


#
