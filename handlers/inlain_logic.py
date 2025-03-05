# callback-хендлеры. Обработка логики inlain кнопок.
from aiogram import types, Router, F
from filters.chat_types import ChatTypeFilter
from aiogram.types import FSInputFile, CallbackQuery, Message
# импорт для машины состояний
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Order

# Кастомные импорты
from text_message import text
from kbds import inline, reply


# Помещаем этот файл в переменную для возможности импорта в основной файл.
inlain_logic_router = Router()
# Наш кастомный фильтр. Если стоит private это значит функционал этого файла
# используется только в чатах. Если gropup то в группах или оба сразу.
inlain_logic_router.message.filter(ChatTypeFilter(["private"]))


class UserState(StatesGroup):
    platform = State()
    bot_type = State()
    wishes = State()
    name = State()
    contacts = State()


# _____________Хендлеры кнопки "заказать разработку бота"___________________
# Выбор платформы
@inlain_logic_router.callback_query(F.data.startswith("platform"))
async def handle_platform_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    if not callback.data:
        return

    platform_name = callback.data.split("_")[1]
    if isinstance(callback.message, types.Message):
        await state.update_data(platform=platform_name)

        await callback.message.edit_text(
            f"Вы выбрали {platform_name.capitalize()}. Выберите тип бота:",
            reply_markup=inline.platform_services_kb
        )
        await state.set_state(UserState.bot_type)
        await callback.answer()


# Выбор бота
@inlain_logic_router.callback_query(F.data.startswith("service_"))
async def handle_service_order(callback: types.CallbackQuery, state: FSMContext):
    if not callback.data:
        return

    bot_type = callback.data.split("_")[1]
    if isinstance(callback.message, types.Message):
        await state.set_state(UserState.wishes)
        await state.update_data(bot_type=bot_type)
        await callback.message.edit_text(
            text.selling_text_7, reply_markup=inline.inline_back_selection
        )
        await callback.answer()


# Пожелания
@inlain_logic_router.message(UserState.wishes, F.text)
async def save_wishes(message: types.Message, state: FSMContext):
    await state.update_data(wishes=message.text)
    await state.set_state(UserState.name)
    await message.answer("Введите ваше имя")


@inlain_logic_router.message(UserState.name, F.text)
async def handle_save_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserState.contacts)
    await message.answer("Введите контактные данные (номер телефона, Telegram):")


@inlain_logic_router.message(UserState.contacts, F.text)
async def handle_save_contacts(message: types.Message, state: FSMContext):
    await state.update_data(contacts=message.text)
    await state.set_state(UserState.contacts)
    await message.answer("Спасибо! Ваш заказ почти готов. Осталось только нажать кнопку 'Оформить заказ'.",
                         reply_markup=inline.inline_back_selection)


# # Хендлер для кнокпи "другие услуги" при выборе бота
# @inlain_logic_router.callback_query(F.data.startswith("text_service_other"))
# async def handle_text_service_order(callback: types.CallbackQuery, state: FSMContext):
#     if not callback.data:
#         return

#     wishes = callback.data.split("_")[1]
#     if isinstance(callback.message, types.Message):
#         await state.update_data(bot_type=wishes)
#         await callback.message.edit_text(
#             text.selling_text_7, reply_markup=inline.inline_back_selection
#         )
#         await state.set_state(OrderState.wishes)
#         await callback.answer()


# Хендлер оформления заказа
@inlain_logic_router.callback_query(F.data == "arrange_order")
async def confirm_order(callback: types.CallbackQuery, state: FSMContext, session: AsyncSession):
    if isinstance(callback.message, types.Message):
        # Получаем все данные, которые пользователь вводил ранее
        data = await state.get_data()
        print("Данные заказа:", data)

        new_order = Order(
            user_id=callback.from_user.id,
            name=data.get("name"),
            platform=data.get("platform"),
            bot_type=data.get("bot_type"),
            wishes=data.get("wishes"),
            contacts=data.get("contacts")
        )

        session.add(new_order)
        # Сохраняем данные в БД
        await session.commit()
        await callback.message.edit_text("Ваш заказ успешно оформлен! Мы свяжемся с вами в ближайшее время.")

        # Очищаем состояние, так как заказ уже оформлен
        await state.clear()
        await callback.answer()


# # Хендлер для кнокпи "другие услуги" при выборе бота
# @inlain_logic_router.callback_query(F.data.startswith("text_service_other"))
# async def handle_text_service_order(callback: types.CallbackQuery, state: FSMContext):
#     if isinstance(callback.message, types.Message):
#         await callback.message.edit_text(
#             text.selling_text_2, reply_markup=inline.inline_back_selection
#         )
#     await callback.answer()


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
    message_text = f"{text.sample_url_text}\n\n🔗 [Перейти в группу]({group_link})"

    await callback.message.answer(
        message_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=inline.inline_back_1,  # Вот здесь теперь передаём клавиатуру
    )
    await callback.answer()  # Просто закрываем "часики"


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


# Варианты меню. Пример картинки.
@inlain_logic_router.callback_query(F.data == "other_menu")
async def handle_sample_menu(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.answer(
            "Посмотрет какие бывают меню 🧐 И выберите любое для проверки",
            reply_markup=inline.inline_menu_options,
        )
        await callback.answer()


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


@inlain_logic_router.callback_query(F.data == "back_main_menu_inline")
async def handle_back_main_menu(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.answer("📌 Вы уже в главном меню. Выберите пункт ниже:",
                                      reply_markup=inline.inline_keyboard_main
                                      )


# inline меню для кнопки "Назад в главное меню"
# Работает для так же для reply, дублирует её.
@inlain_logic_router.callback_query(F.data == "back_main_inlain")
async def back_to_main_inlain(callback: types.CallbackQuery):
    if isinstance(callback.message, types.Message):
        photo = FSInputFile("images/reply.webp")
        await callback.message.answer(text.selling_text_4, reply_markup=reply.submenu_markup)
        await callback.message.answer_photo(photo)
        await callback.answer()
        # # Редактируем inline-клавиатуру
        # await callback.message.edit_text(
        #     "📌 Всё просто: изучаете — выбираете нужное решение — оформляете заказ! Выберите пункт меню ниже",
        #     reply_markup=inline.inline_keyboard_main
        # )


# Хендлер для inline кнопки "Назад к выбору платформы"
@inlain_logic_router.callback_query(F.data.in_(["arrange_back", "back_to_platforms"]))
async def back_to_platforms(callback: types.CallbackQuery):
    if isinstance(callback.message, types.Message):  # Проверяем, доступно ли сообщение
        await callback.message.edit_text(
            "Выберите платформу:", reply_markup=inline.platform_kb
        )
    await callback.answer()


# # ____________________Обработка действий главного меню___________________________
# @inlain_logic_router.callback_query(F.data == "main_variants")
# async def inline_menu_options(callback: types.CallbackQuery):
#     if isinstance(callback.message, types.Message):
#         photo = FSInputFile("images/start_image_2.webp")
#         await callback.message.answer_photo(
#             photo,
#             "Посмотрите какие бывают меню 🧐 И выберите любое для проверки",
#             reply_markup=inline.inline_menu_options,
#         )


# # Обработка действий главного меню
# @inlain_logic_router.callback_query(F.data == "main_reviews")
# async def inline_main_menu_reviews(callback: types.CallbackQuery):
#     if isinstance(callback.message, types.Message):
#         photo = FSInputFile("images/review1.webp")
#         photo_2 = FSInputFile("images/review1.webp")
#         await callback.message.answer_photo(photo)
#         await callback.message.answer_photo(photo_2)
#         await callback.message.answer("🔹 Лучшие отзывы моих клиентов. 📌 Открываю главное меню",
#                                       reply_markup=inline.inline_keyboard_back_main_menu)


# # Обработка действий главного меню
# @inlain_logic_router.callback_query(F.data == "main_options")
# async def inline_main_menu_options_payment(callback: types.CallbackQuery):
#     if isinstance(callback.message, types.Message):
#         await callback.message.answer(text.selling_text, reply_markup=inline.inline_keyboard_back_main_menu)


# # Обработка действий главного меню
# @inlain_logic_router.callback_query(F.data == "main_cost_")
# async def inline_main_menu_cost(callback: types.CallbackQuery):
#     if isinstance(callback.message, types.Message):
#         await callback.message.answer(text.selling_text_3, reply_markup=inline.inline_keyboard_back_main_menu)
