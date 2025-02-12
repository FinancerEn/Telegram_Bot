# # Кнопки (без логики обработки)
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.types import InlineKeyboardButton


# # Создаём кнопки
# button_telegram = InlineKeyboardButton(text="Telegram", callback_data="platform_telegram")
# button_instagram = InlineKeyboardButton(text="Instagram", callback_data="platform_instagram")
# button_vk = InlineKeyboardButton(text="Вконтакте", callback_data="platform_vk")
# button_whatsapp = InlineKeyboardButton(text="Whatsapp", callback_data="platform_whatsapp")
# button_other = InlineKeyboardButton(text="Другое", callback_data="platform_other")

# # Создаём inline-клавиатуру и добавляем кнопки
# builder = InlineKeyboardBuilder()
# builder.button(text="Telegram", callback_data="platform_telegram")
# builder.button(text="Instagram", callback_data="platform_instagram")
# builder.button(text="Вконтакте", callback_data="platform_vk")
# builder.button(text="Whatsapp", callback_data="platform_whatsapp")
# builder.button(text="Другое", callback_data="platform_other")

# platform_kb = builder.as_markup()


# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# platform_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Меню", callback_data="menu"),
#         InlineKeyboardButton(text="Отзывы", callback_data="reviews"),
#         InlineKeyboardButton(text="Кейсы", callback_data="cases"),
#     ],
#     [
#         InlineKeyboardButton(text="Заказать разработку бота", callback_data="order"),
#         InlineKeyboardButton(text="Стоимость услуг", callback_data="prices"),
#     ],  # ← Здесь добавил запятую!
#     [
#         InlineKeyboardButton(text='Алёрт', callback_data='show_alert')
#     ]
# ])
