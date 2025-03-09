from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


# Определяем CallbackData для платформ
class PlatformCallback(CallbackData, prefix="platform"):
    name: str  # telegram, instagram, vk, whatsapp, other


# Определяем CallbackData для выбора услуги
class ServiceCallback(CallbackData, prefix="service"):
    name: str  # vizitka, quiz, catalog, webinar, other


class selectionCallback(CallbackData, prefix="arrange"):
    name: str


# Создаем inline-клавиатуру с кнопками в столбик и в два столбика
# Где row_width=1 означает, что каждая кнопка будет в отдельном ряду.
# callback_data — это строка, которая будет передана боту при нажатии на кнопку.
# service_vizitka — это просто строка, которую мы придумали сами. Её смысл:
# service — может означать "тип услуги", vizitka — конкретный вид услуги (например, "бот-визитка").
# При нажатии на кнопку "Чат-бот визитка" с callback_data="service_vizitka" в callback_query.data
# прилетит строка "service_vizitka", которую можно обработать в хендлере.

inline_keyboard_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Варианты меню", callback_data="main_variants")],
        [InlineKeyboardButton(text="Отзывы", callback_data="main_reviews")],
        [InlineKeyboardButton(text="Оплата и процесс работы", callback_data="main_options")],
        [InlineKeyboardButton(text="Стоимость", callback_data="main_cost_")],
        [InlineKeyboardButton(text="Заказать разработку бота", callback_data="main_development")],
    ],
)

platform_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💬 Telegram", callback_data="platform_telegram")],
        [InlineKeyboardButton(text="📸 Instagram", callback_data="platform_instagram")],
        [InlineKeyboardButton(text="📲 ВКонтакте", callback_data="platform_vk")],
        [InlineKeyboardButton(text="☎️ WhatsApp", callback_data="platform_whatsapp")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_main_inlain")],
    ]
)


platform_services_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Чат-бот визитка", callback_data="service_vizitka")],
        [
            InlineKeyboardButton(
                text="Квиз-бот - опросник", callback_data="service_quiz"
            )
        ],
        [
            InlineKeyboardButton(
                text="Товарный бот - каталог", callback_data="service_catalog"
            )
        ],
        [
            InlineKeyboardButton(
                text="Автовебинарный бот", callback_data="service_webinar"
            )
        ],
        [InlineKeyboardButton(text="Другие услуги", callback_data="text_service_other")],
        [
            InlineKeyboardButton(
                text="🔙 Назад к выбору платформы", callback_data="back_to_platforms"
            )
        ],
    ]
)

inline_back_selection = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Оформить заказ", callback_data="arrange_order")],
        [InlineKeyboardButton(text="Назад к выбору платформы", callback_data="arrange_back")],
    ],
)

inline_back_selection_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пропустить, далее⏩", callback_data="next_order")],
        [InlineKeyboardButton(text="Назад к выбору платформы", callback_data="arrange_back")],
    ],
)

inline_back_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад к примерам", callback_data="back_menu")],
    ],
)

inline_menu_options = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="inline меню", callback_data="inline_menu")],
        [InlineKeyboardButton(text="reply меню", callback_data="reply_menu")],
        [InlineKeyboardButton(text="Стандартное меню", callback_data="standard_back")],
    ],
)

inline_options = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пример Ссылки", callback_data="link_resource")],
        [
            InlineKeyboardButton(
                text="Пример Текста", callback_data="text_button"
            )
        ],
        [
            InlineKeyboardButton(
                text="Пример Картинки", callback_data="image_button"
            )
        ],
        [
            InlineKeyboardButton(
                text="Пример меню", callback_data="other_menu"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 Назад к выбору меню", callback_data="back_to_menu"
            )
        ],
    ]
)

inline_keyboard_back_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад в главное меню", callback_data="back_main_menu_inline")],
    ],
)


# # _______________Инлайн кнопки в один ряд________________
# # Кнопки (без логики обработки)
# from aiogram.utils.keyboard import InlineKeyboardBuilder

# # Создаём inline-клавиатуру и добавляем кнопки
# builder = InlineKeyboardBuilder()
# builder.button(text="Telegram", callback_data="platform_telegram")
# builder.button(text="Instagram", callback_data="platform_instagram")
# builder.button(text="Вконтакте", callback_data="platform_vk")
# builder.button(text="Whatsapp", callback_data="platform_whatsapp")
# builder.button(text="Другое", callback_data="platform_other")

# platform_kb = builder.as_markup()
