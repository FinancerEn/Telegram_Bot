from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


# Определяем CallbackData для платформ
class PlatformCallback(CallbackData, prefix="platform"):
    name: str  # telegram, instagram, vk, whatsapp, other


# Определяем CallbackData для выбора услуги
class ServiceCallback(CallbackData, prefix="service"):
    name: str  # vizitka, quiz, catalog, webinar, other


class PriceCallback(CallbackData, prefix="price"):
    name: str  # vizitka, quiz, catalog, webinar, other


class Cases_Callback(CallbackData, prefix="cases"):
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
        [InlineKeyboardButton(text="Какие бывают боты, стоимость", callback_data="main_cost_")],
        [InlineKeyboardButton(text="Заказать разработку бота", callback_data="main_development")],
    ],
)

platform_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💬 Telegram", callback_data="platform_telegram")],
        [InlineKeyboardButton(text="📸 Instagram", callback_data="platform_instagram")],
        [InlineKeyboardButton(text="📲 ВКонтакте", callback_data="platform_vk")],
        [InlineKeyboardButton(text="☎️ WhatsApp", callback_data="platform_whatsapp")],
        [InlineKeyboardButton(text="🔙 Отменить и выйти", callback_data="cancel_order")],
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
        [
            InlineKeyboardButton(
                text="🛒 Чат-бот Магазин", callback_data="service_shop_bott"
            )
        ],
        [
            InlineKeyboardButton(
                text="📝 Бот-запись на услуги", callback_data="service_record_bott"
            )
        ],
        [
            InlineKeyboardButton(
                text="HR-бот", callback_data="service_hr_bott"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 Назад к выбору платформы", callback_data="back_to_platforms"
            )
        ],
    ]
)

platform_services_price_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📇 Чат-бот Визитка", callback_data="price_vizitka")],
        [
            InlineKeyboardButton(
                text="❓ Квиз-бот (Опросник, Тест, Игра)", callback_data="price_quiz"
            )
        ],
        [
            InlineKeyboardButton(
                text="📦 Товарный Бот (Каталог)", callback_data="price_catalog"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎥 Автовебинарный Бот", callback_data="price_webinar"
            )
        ],
        [
            InlineKeyboardButton(
                text="🛒 Чат-бот Магазин", callback_data="price_shop"
            )
        ],
        [
            InlineKeyboardButton(
                text="📝 Бот-запись на услуги", callback_data="price_record_bott"
            )
        ],
        [
            InlineKeyboardButton(
                text="🕓 HR-бот (поиск сотрудников)", callback_data="price_hr_bott"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔧 Другие услуги:", callback_data="price_other")
        ],
        [
            InlineKeyboardButton(
                text="🔙 Назад к началу", callback_data="back_main_inlain"
            )
        ],
    ]
)

platform_cases_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📇 Чат-бот Визитка", callback_data="cases_vizitka")],
        [
            InlineKeyboardButton(
                text="❓ Квиз-бот (Опросник, Тест, Игра)", callback_data="cases_quiz"
            )
        ],
        [
            InlineKeyboardButton(
                text="📦 Товарный Бот (Каталог)", callback_data="cases_catalog"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎥 Автовебинарный Бот", callback_data="cases_webinar"
            )
        ],
        [
            InlineKeyboardButton(
                text="🛒 Чат-бот Магазин", callback_data="cases_shop"
            )
        ],
        [
            InlineKeyboardButton(
                text="📝 Бот-запись на услуги", callback_data="cases_record_bott"
            )
        ],
        [
            InlineKeyboardButton(
                text="🕓 HR-бот (поиск сотрудников)", callback_data="cases_hr_bott"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔧 Другие услуги:", callback_data="cases_other")
        ],
        [
            InlineKeyboardButton(
                text="🔙 Назад к началу", callback_data="back_main_inlain"
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
        [InlineKeyboardButton(text="🔙 Назад к выбору платформы", callback_data="arrange_back")],
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
        [InlineKeyboardButton(text="🔙 Назад к началу", callback_data="back_main_inlain")],
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
        # [
        #     InlineKeyboardButton(
        #         text="Пример меню", callback_data="other_menu"
        #     )
        # ],
        [
            InlineKeyboardButton(
                text="🔙 Вернуться к выбору примера меню", callback_data="back_to_menu"
            )
        ],
    ]
)

inline_keyboard_back_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад в главное меню", callback_data="back_main_price_inline")],
    ],
)

exit_button_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❌ Отменить и выйти", callback_data="cancel_order")],
    ],
)

exit_button_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 На шаг назад", callback_data="step_backk")],
    ],
)

back_platform = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Назад к выбору платформы", callback_data="back_to_platforms"
            )
        ],
    ],
)

back_platform = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Назад к списку кейсов", callback_data="back_list_bots"
            )
        ],
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
