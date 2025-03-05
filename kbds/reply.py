# ReplyKeyboardMarkup — это специальный объект из библиотеки aiogram, который описывает разметку (markup) кнопок для клавиатуры Telegram.
# KeyboardButton Формируем клавиатуру.
# Используй ReplyKeyboardMarkup, когда тебе нужна простая клавиатура, которая:
# ✔ Автоматически отправляет текст кнопки в чат.
# ✔ Закрепляется под полем ввода сообщений.
# ✔ Может изменяться в зависимости от диалога с пользователем.
# ✔ Работает только в приватных чатах (не в группах!).
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура для администратора
ADMIN_KB = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Создать заказ"), KeyboardButton(text="Удалить заказ")],
        [KeyboardButton(text="Просмотр заказов"), KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True,
    sizes=(2,),
)


submenu_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Варианты меню"),
            KeyboardButton(text="Отзывы"),
        ],
        [
            KeyboardButton(text="Оплата и процесс работы"),
            KeyboardButton(text="Стоимость"),
        ],
        [
            KeyboardButton(text="Заказать разработку бота"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Что Вас интересует?",
)


reply_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telegram"),
            KeyboardButton(text="Instagram"),
        ],
        [
            KeyboardButton(text="ВКонтакте"),
            KeyboardButton(text="Whatsapp"),
        ],
        [
            KeyboardButton(text="Другое"),
            KeyboardButton(text="назад"),
        ],
    ],
    resize_keyboard=True,
)


reply_markup_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Чат-бот визитка"),
        ],
        [
            KeyboardButton(text="Квиз-ботэто - опросник"),
        ],
        [
            KeyboardButton(text="Товарный бот - бот каталог"),
        ],
        [
            KeyboardButton(text="Автовебинарный бот"),
        ],
        [
            KeyboardButton(text="Другие услуги"),
        ],
        [
            KeyboardButton(text="Назад к выбору платформы"),
        ],
    ],
    resize_keyboard=True,
)


back_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оформить заказ"),
        ],
        [
            KeyboardButton(text="Назад"),
        ],
    ],
    resize_keyboard=True,
)


back_selection = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оформить заказ"),
        ],
        [
            KeyboardButton(text="Назад к выбору платформы"),
        ],
    ],
    resize_keyboard=True,
)


back_markup_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Далее"),
        ],
        [
            KeyboardButton(text="Назад"),
        ],
    ],
    resize_keyboard=True,
)


decoration_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
        ],
        [
            KeyboardButton(text="Назад"),
        ],
    ],
    resize_keyboard=True,
)


cancellation_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отмена"),
        ],
        [
            KeyboardButton(text="Назад_"),
        ],
    ],
    resize_keyboard=True,
)


last_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оформляем заказ"),
        ],
        [
            KeyboardButton(text="Назад"),
        ],
    ],
    resize_keyboard=True,
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
