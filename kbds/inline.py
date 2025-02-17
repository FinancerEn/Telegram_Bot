from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создаем inline-клавиатуру с кнопками в столбик и в два столбика
# Где row_width=1 означает, что каждая кнопка будет в отдельном ряду.
platform_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💬 Telegram", callback_data="platform_telegram"),
            InlineKeyboardButton(text="📸 Instagram", callback_data="platform_instagram")
        ],
        [
            InlineKeyboardButton(text="📲 ВКонтакте", callback_data="platform_vk"),
            InlineKeyboardButton(text="☎️ WhatsApp", callback_data="platform_whatsapp")
        ],
        [
            InlineKeyboardButton(text="🔍 Другое", callback_data="platform_other")
        ]
    ]
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
