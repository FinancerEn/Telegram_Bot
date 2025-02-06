# Файл Меню: ReplyKeyboardMarkup - ответная клавиатура, KeyboardButton Формируем клавиатуру.
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


submenu_kd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="меню"),
            KeyboardButton(text="Отзывы"),
            KeyboardButton(text="Кейсы"),
        ],
        [
            KeyboardButton(text="Заказать разработку бота"),
            KeyboardButton(text="Стоимость услуг"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?',
)


# start_kbd2 = ReplyKeyboardBuilder
# start_kbd2.add(
#     KeyboardButton(text="меню"),
#     KeyboardButton(text="Отзывы"),
#     KeyboardButton(text="Кейсы"),
#     KeyboardButton(text="Заказать разработку бота"),
#     KeyboardButton(text="Стоимость услуг"),
# )
# start_kbd2.adjust(2, 3)


# start_kbd3 = ReplyKeyboardBuilder
# start_kbd3.attach(start_kbd2)
# start_kbd3.row(KeyboardButton(text="Оставить отзыв"))
