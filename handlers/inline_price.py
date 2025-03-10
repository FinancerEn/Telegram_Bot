# Файл кнопки стоимость
from aiogram import types, Router, F
from filters.chat_types import ChatTypeFilter
from aiogram.types import FSInputFile

# Кастомные импорты
from text_message import text
from kbds import inline, reply

inlain_price_router = Router()
inlain_price_router.message.filter(ChatTypeFilter(["private"]))


@inlain_price_router.callback_query(F.data.startswith("price_vizitka"))
async def handle_price_vizitka(callback: types.CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer(text.business_card_text, reply_markup=reply.submenu_markup)
        await callback.message.answer_photo(photo)
        await callback.message.answer(
            "Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data.startswith("price_quiz"))
async def handle_price_quiz(callback: types.CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer(text.questionnaire_text, reply_markup=reply.submenu_markup)
        await callback.message.answer_photo(photo)
        await callback.message.answer(
            "Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data.startswith("price_catalog"))
async def handle_price_catalog(callback: types.CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer(text.commodity_text, reply_markup=reply.submenu_markup)
        await callback.message.answer_photo(photo)
        await callback.message.answer(
            "Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data.startswith("price_webinar"))
async def handle_price_webinar(callback: types.CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer(text.webinar_text, reply_markup=reply.submenu_markup)
        await callback.message.answer_photo(photo)
        await callback.message.answer(
            "Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data.startswith("price_shop"))
async def handle_price_shop(callback: types.CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer(text.webinar_text, reply_markup=reply.submenu_markup)
        await callback.message.answer_photo(photo)
        await callback.message.answer(
            "Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()


@inlain_price_router.callback_query(F.data.startswith("price_other"))
async def handle_price_other(callback: types.CallbackQuery):
    if callback.message:
        photo = FSInputFile("images/start_image_2.webp")
        await callback.message.answer(text.other_text, reply_markup=reply.submenu_markup)
        await callback.message.answer_photo(photo)
        await callback.message.answer(
            "Нажмите если нужно вернуться назад к списку ботов",
            reply_markup=inline.inline_keyboard_back_main_menu,
        )
        await callback.answer()
