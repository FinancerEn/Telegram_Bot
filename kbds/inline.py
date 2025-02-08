# Кнопки (без логики обработки)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


# Создаём кнопки
button_telegram = InlineKeyboardButton(text="Telegram", callback_data="platform_telegram")
button_instagram = InlineKeyboardButton(text="Instagram", callback_data="platform_instagram")
button_instagram = InlineKeyboardButton(text="Вконтакте", callback_data="platform_Вконтакте")
button_instagram = InlineKeyboardButton(text="Whatsapp", callback_data="platform_Whatsapp")
button_instagram = InlineKeyboardButton(text="Другое", callback_data="platform_Другое")

# Создаём inline-клавиатуру и добавляем кнопки
builder = InlineKeyboardBuilder()
builder.button(text="Telegram", callback_data="platform_telegram")
builder.button(text="Instagram", callback_data="platform_instagram")
builder.button(text="Вконтакте", callback_data="platform_vk")
builder.button(text="Whatsapp", callback_data="platform_whatsapp")
builder.button(text="Другое", callback_data="platform_other")

platform_kb = builder.as_markup()

# def get_callback_btns(
#         *,
#         btns: dict[str, str],
#         sizes: tuple[int] = (2,)):

#     keyboard = InlineKeyboardBulder()

#     for text, data in btns.items():

#         keyboard.add(InlineKeyboardButton(text=text, callback_data=data))

#     return keyboard.adjust(*sizes).as_markup()


# def get_url_btns(
#         *,
#         btns: dict[str, str],
#         sizes: tuple[int] = (2,)):

#     keyboard = InlineKeyboardBulder()

#     for text, url in btns.items():

#         keyboard.add(InlineKeyboardButton(text=text, url=url))

#     return keyboard.adjust(*sizes).as_markup()


# # Создать микс из CallBack и URL кнопок
# def get_inlineMix_btns(
#     *,
#     btns: dict[str, str],
#     sizes: tuple[int] = (2,)):

#     Keyboard = InlineKeyboardBulder()

#     for text, value in btns.items():
#         if '://' in value:
#             Keyboard.add(InlineKeyboardButton(text=text, url=value))
#         else:
#             Keyboard.add(InlineKeyboardButton(text=text, callback_data=value))

#     return Keyboard.adjust(*sizes).as_markup()
