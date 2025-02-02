from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f


# Помещаем этот файл в переменную для возможности импорта в основной файл.
user_private_router = Router()


# dp.message - декоратор обработки событий приходящих к боту.
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет! Я — ваш Чат-бот Разработчик. Чем могу помочь?')
    # Ответить с упоминанием автора код: await message.reply(message.text)


@user_private_router.message(or_f(Command('menu'), F.text.casefold() == 'меню'))
async def menu_cmd(message: types.Message):
    await message.answer("Меню:")


@user_private_router.message(or_f(Command('cost'), F.text.casefold() == 'стоимость'))
async def cost_cmd(message: types.Message):
    await message.answer("Стоимость:")


@user_private_router.message(or_f(Command('payment'), F.text.casefold() == 'варианты оплаты'))
async def payment_cmd(message: types.Message):
    await message.answer("Варианты оплаты:")


@user_private_router.message(or_f(Command('about'), F.text.casefold() == 'о нас'))
async def about_cmd(message: types.Message):
    await message.answer('О нас:')


@user_private_router.message(or_f(Command('shipping'), F.text.casefold().contains('доставк')))
async def new_menu_cmd(message: types.Message):
    await message.answer("Варианты доставки")




# Генерируем ответ на определённые ключевые слова
# @user_private_router.message(lambda message: message.content_type == types.ContentType.TEXT)
# async def echo(message: types.Message):
#     text = message.text

#     if text:  # Проверяем, что text не None
#         if text.lower() in ['привет', 'здравствуйте', 'добрый день', 'hi', 'hello', 'добрый вечер', 'доброе утро']:
#             await message.answer('Здравствуйте!')
#         elif text.lower() in ['до свидания', 'досвидания', 'пока', 'пакеда', 'прощайте']:
#             await message.answer('До свидания')
#         else:
#             await message.answer(text)
#     else:
#         await message.answer("Сообщение не содержит текста.")
