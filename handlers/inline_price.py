# Файл кнопки стоимость
from aiogram import Router, F
from filters.chat_types import ChatTypeFilter
from aiogram.types import FSInputFile, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кастомные импорты
from text_message import text
from kbds import inline, reply

inlain_price_router = Router()
inlain_price_router.message.filter(ChatTypeFilter(["private"]))


@inlain_price_router.callback_query(F.data == "price_vizitka")
async def handle_price_vizitka(callback: CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer_photo(
            photo, text.business_card_text, reply_markup=reply.submenu_markup
        )
        await callback.message.answer(
            "⏮️ Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data == "price_quiz")
async def handle_price_quiz(callback: CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer_photo(
            photo, text.questionnaire_text, reply_markup=reply.submenu_markup
        )
        await callback.message.answer(
            "⏮️ Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data == "price_catalog")
async def handle_price_catalog(callback: CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer_photo(
            photo, text.catalog_text, reply_markup=reply.submenu_markup
        )
        await callback.message.answer(
            "⏮️ Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data == "price_webinar")
async def handle_price_webinar(callback: CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer_photo(
            photo, text.webinar_text, reply_markup=reply.submenu_markup
        )
        await callback.message.answer(
            "⏮️ Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data == "price_shop")
async def handle_price_shop(callback: CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer_photo(
            photo, text.shopbot_text, reply_markup=reply.submenu_markup
        )
        await callback.message.answer(
            "⏮️ Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data == "price_record_bott")
async def handle_record_bott(callback: CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer_photo(
            photo, text.popular_types_text, reply_markup=reply.submenu_markup
        )
        await callback.message.answer(
            "⏮️ Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data == "price_hr_bott")
async def handle_hr_bott(callback: CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer_photo(
            photo, text.hr_bot_text, reply_markup=reply.submenu_markup
        )
        await callback.message.answer(
            "⏮️ Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data == "price_other")
async def handle_price_other(callback: CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer_photo(
            photo, text.other_text, reply_markup=reply.submenu_markup
        )
        await callback.message.answer(
            "⏮️ Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


# _________________________Хендлеры кнокпи "Кейсы"__________________________
@inlain_price_router.callback_query(F.data == "cases_vizitka")
async def cases_vizitka_link(callback: CallbackQuery):
    if callback.message is None:
        await callback.answer("Ошибка: Не удалось обработать запрос.", show_alert=True)
        return

    group_link = "https://t.me/+DDiXtpAlb7AxZmIy"
    message_text = f"{text.business_card_double}{text.cases_text_2}"

    # Создаём inline-кнопку со ссылкой, добавляем ещё одну существующую клавиатуру inline.back_platform
    # и возвращаем хендлером сразу 2 клавиатуры.
    link_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Перейти в бота", url=group_link)],
        ] + inline.back_platform.inline_keyboard  # Добавляем кнопки из второй клавиатуры
    )

    await callback.message.answer(
        message_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=link_button,  # Вот здесь теперь передаём клавиатуру
    )
    await callback.answer()  # Просто закрываем "часики"


@inlain_price_router.callback_query(F.data == "cases_quiz")
async def cases_quiz_link(callback: CallbackQuery):
    if callback.message is None:
        await callback.answer("Ошибка: Не удалось обработать запрос.", show_alert=True)
        return

    group_link = "https://t.me/+DDiXtpAlb7AxZmIy"
    message_text = f"{text.questionnaire_text_double}{text.cases_text_2}"

    link_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Перейти в бота", url=group_link)],
        ] + inline.back_platform.inline_keyboard
    )

    await callback.message.answer(
        message_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=link_button,
    )
    await callback.answer()


@inlain_price_router.callback_query(F.data == "cases_catalog")
async def cases_catalog_link(callback: CallbackQuery):
    if callback.message is None:
        await callback.answer("Ошибка: Не удалось обработать запрос.", show_alert=True)
        return

    group_link = "https://t.me/+DDiXtpAlb7AxZmIy"
    message_text = f"{text.catalog_text_double}{text.cases_text_2}"

    link_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Перейти в бота", url=group_link)],
        ] + inline.back_platform.inline_keyboard
    )
    await callback.message.answer(
        message_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=link_button,
    )
    await callback.answer()


@inlain_price_router.callback_query(F.data == "cases_webinar")
async def cases_webinar_link(callback: CallbackQuery):
    if callback.message is None:
        await callback.answer("Ошибка: Не удалось обработать запрос.", show_alert=True)
        return

    group_link = "https://t.me/+DDiXtpAlb7AxZmIy"
    message_text = f"{text.webinar_tex_double}{text.cases_text_2}"

    link_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Перейти в бота", url=group_link)],
        ] + inline.back_platform.inline_keyboard
    )

    await callback.message.answer(
        message_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=link_button,
    )
    await callback.answer()


@inlain_price_router.callback_query(F.data == "cases_shop")
async def cases_shop_link(callback: CallbackQuery):
    if callback.message is None:
        await callback.answer("Ошибка: Не удалось обработать запрос.", show_alert=True)
        return

    group_link = "https://t.me/+DDiXtpAlb7AxZmIy"
    message_text = f"{text.shopbot_text_double}{text.cases_text_2}"

    link_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Перейти в бота", url=group_link)],
        ] + inline.back_platform.inline_keyboard
    )

    await callback.message.answer(
        message_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=link_button,
    )
    await callback.answer()


@inlain_price_router.callback_query(F.data == "cases_record_bott")
async def cases_record_bott_link(callback: CallbackQuery):
    if callback.message is None:
        await callback.answer("Ошибка: Не удалось обработать запрос.", show_alert=True)
        return

    group_link = "https://t.me/+DDiXtpAlb7AxZmIy"
    message_text = f"{text.popular_types_text_double}{text.cases_text_2}"

    link_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Перейти в бота", url=group_link)],
        ] + inline.back_platform.inline_keyboard
    )

    await callback.message.answer(
        message_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=link_button,
    )
    await callback.answer()


@inlain_price_router.callback_query(F.data == "cases_hr_bott")
async def cases_hr_bott_link(callback: CallbackQuery):
    if callback.message is None:
        await callback.answer("Ошибка: Не удалось обработать запрос.", show_alert=True)
        return

    group_link = "https://t.me/+DDiXtpAlb7AxZmIy"
    message_text = f"{text.hr_bot_text_double}{text.cases_text_2}"

    link_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Перейти в бота", url=group_link)],
        ] + inline.back_platform.inline_keyboard
    )

    await callback.message.answer(
        message_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=link_button,
    )
    await callback.answer()


@inlain_price_router.callback_query(F.data == "cases_other")
async def cases_other_link(callback: CallbackQuery):
    if callback.message is None:
        await callback.answer("Ошибка: Не удалось обработать запрос.", show_alert=True)
        return

    group_link = "https://t.me/+DDiXtpAlb7AxZmIy"
    message_text = f"{text.other_text}{text.cases_text_2}"

    link_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Перейти в бота", url=group_link)],
        ] + inline.back_platform.inline_keyboard
    )

    await callback.message.answer(
        message_text,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=link_button,
    )
    await callback.answer()
