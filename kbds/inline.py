# from aiogram.types import InlineKeyboardBulder, InlineKeyboardButton


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
