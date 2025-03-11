selling_text = """Для какой платформы вам нужен чат-бот?

🤖Выберите платформу в меню или напечатайте в поле ввода сообщения
"""

selling_text_2 = """ Какая у вас сфера деятельности и как вы планируете использовать чат-бота?
Напишите в поле ввода сообщений или выберите кнопку меню:

"""

selling_text_3 = """

Чат-бот визитка (от 3500 руб.)
📌 Задача: Быстро представить компанию или специалиста, рассказать о его услугах.
💡 Пример использования: Владелец салона красоты отправляет клиентам ссылку на бота, который представляет услуги, цены и контактные данные.
🛠 Техническая реализация:

Пользователь заходит в бота и видит приветственное сообщение с описанием услуг.
Может нажать кнопки для просмотра портфолио, оставить заявку или получить ссылку на соцсети.
Реализуется через aiogram или pyTelegramBotAPI с базой данных SQLite.
Цена:
- до 20 блоков - 3500;
- до 30 блоков - 5000;
- от 30 блоков - 5000 + доплата за каждый блок 200р.

Квиз-бот (от 3000 руб.)
📌 Задача: Интерактивный тест для сбора контактов потенциальных клиентов (лидогенерация).
💡 Пример использования: Агентство недвижимости предлагает пользователю пройти тест, в конце которого он оставляет контакты для подбора квартиры.
🛠 Техническая реализация:

Бот задаёт 5-7 вопросов, запоминая ответы.
После последнего вопроса предлагает оставить телефон/e-mail.
Информация отправляется в Google Sheets, CRM-систему или в телеграмм группу.


Для чего используется квиз - бот:

- для полной автоматизации общения с клиентом без вашего участия;
- для создания нескольких сценариев при опросе , в зависимости от того , что клиент отвечает;
- для структурирования медиафайлов, видео и т.п. для наглядности;
- для подключения онлайн оплаты / каталогов
- квиз бот может стать частью другого бота

Подходит для любых сфер бизнеса.
Недвижимость не исключение!

Цена:
- до 10 блоков - 3000;
- до 20 блоков - 5000;
- до 30 блоков - 7000;
- от 30 блоков - 7000 + доплата за каждый блок 200р.

Товарный бот - бот каталог - один из видов бота-визитки,
стоимость данного бота зависит от количества товарных позиций
(один товар - описание и макеты, либо один товар имеет несколько подвидов,
соответсвенно, описание и макеты - подвид считается товаром).

Для каких сфер используется бот каталог:
- Онлайн - магазин;
- Для различных бутиков и тд.;
- Каталог товаров для сетевого бизнеса (орифлейм, эйвон, фаберлик, гринвей, NL и тд.).

Цена:
- до 10 товаров - 4000;
- до 20 товаров - 7000;
- до 30 товаров - 10000;
- от 30 товаров - 10000 + доплата за каждый блок 300р.

Автовебинарный бот - бот содержащий воронку продаж, одним из этапов которого является автовебинар.

Любая воронка продаж состоит из нескольких этапов. Автоворонка для мастер-класса, вебинара, прямого эфира и тд. состоит из следующих этапов:

- Подписка в воронку;
- Лид-магнит (бесплатный подарок - чек лист, консультация и тд);
- Прогревающая серия контента;
-Трансляция (вебинар, прямой эфир, мастер-класс и тд);
- Запись или повтор;
- Дожимающая серия контента.

Цена:
- до 15 блоков - 5000;
- до 20 блоков - 7000;
- от 20 блоков - 7000 + доплата за каждый блок 200р.

Другие услуги:

- реконструкция бота 1 блок - 400р;
- рассылка по подписчикам внутри бота с кнопками касания - 700р;
"""

cases_text = """📌 Кейсы наших ботов

Здесь вы можете увидеть, как работают разные типы ботов! Просто выберите нужный вариант ниже 👇

После нажатия на ссылку вы получите описание бота и ссылку на его демо-версию 🔗✨
"""

cases_text_2 = """
⏭️ После нажатия на ссылку вы получите описание бота и ссылку на его демо-версию 🔗✨ 👇
"""
business_card_double = """📇 Чат-бот Визитка
📌 Задача: Быстро представить компанию или специалиста, рассказать о его услугах.
💡 Пример использования: Владелец салона красоты отправляет клиентам ссылку на бота, который представляет услуги, цены и контактные данные.
🛠 Техническая реализация:

Пользователь заходит в бота и видит приветственное сообщение с описанием услуг.
Может нажать кнопки для просмотра портфолио, оставить заявку или получить ссылку на соцсети.
Реализуется через aiogram или pyTelegramBotAPI с базой данных SQLite.
"""

business_card_text = """📇 Чат-бот Визитка
🔹 Ваш мини-сайт в мессенджере – мгновенный доступ к информации и удобный способ связи!
🔹 Автоматические ответы на частые вопросы.
🔹 Подключение заказа услуг или товаров.

💰 Цена:
✅ До 20 блоков – 3500 руб.
✅ До 30 блоков – 5000 руб.
✅ Более 30 блоков – 5000 руб. + 200 руб. за каждый дополнительный блок.


📌 Задача: Быстро представить компанию или специалиста, рассказать о его услугах.
💡 Пример использования: Владелец салона красоты отправляет клиентам ссылку на бота, который представляет услуги, цены и контактные данные.
🛠 Техническая реализация:

Пользователь заходит в бота и видит приветственное сообщение с описанием услуг.
Может нажать кнопки для просмотра портфолио, оставить заявку или получить ссылку на соцсети.
Реализуется через aiogram или pyTelegramBotAPI с базой данных SQLite.
"""

questionnaire_text_double = """❓ Квиз-бот (Опросник, Тест, Игра)
📌 Задача: Интерактивный тест для сбора контактов потенциальных клиентов (лидогенерация).
💡 Пример использования: Агентство недвижимости предлагает пользователю пройти тест, в конце которого он оставляет контакты для подбора квартиры.
🛠 Техническая реализация:

Бот задаёт 5-7 вопросов, запоминая ответы.
После последнего вопроса предлагает оставить телефон/e-mail.
Информация отправляется в Google Sheets, CRM-систему или в телеграмм группу.
"""

questionnaire_text = """❓ Квиз-бот (Опросник, Тест, Игра)
🔸 Идеальный инструмент для вовлечения клиентов!
🔸 Автоматический диалог с индивидуальными сценариями.
🔸 Возможность добавления фото, видео, кнопок.
🔸 Подключение онлайн-оплаты и каталогов.

💰 Цена:
✔ До 10 блоков – 3000 руб.
✔ До 20 блоков – 5000 руб.
✔ До 30 блоков – 7000 руб.
✔ Более 30 блоков – 7000 руб. + 200 руб. за каждый дополнительный блок

📌 Задача: Интерактивный тест для сбора контактов потенциальных клиентов (лидогенерация).
💡 Пример использования: Агентство недвижимости предлагает пользователю пройти тест, в конце которого он оставляет контакты для подбора квартиры.
🛠 Техническая реализация:

Бот задаёт 5-7 вопросов, запоминая ответы.
После последнего вопроса предлагает оставить телефон/e-mail.
Информация отправляется в Google Sheets, CRM-систему или в телеграмм группу.
"""

catalog_text_double = """📦 Товарный Бот (Каталог)
📌 Задача: Выгрузка товаров с фото, описанием и фильтрацией по категориям.
💡 Пример использования: Магазин одежды предлагает клиентам выбрать товар прямо в Telegram.
🛠 Техническая реализация:

Пользователь может выбрать категорию, увидеть список товаров, нажать на товар и получить описание.
Хранение данных – SQLite или PostgreSQL.
Бот интегрируется с YooMoney, CloudPayments для приёма платежей.
"""

catalog_text = """📦 Товарный Бот (Каталог)
🛒 Простой и удобный бот-каталог для демонстрации товаров!
🔹 Подходит для магазинов, бутиков, сетевого бизнеса (NL, Oriflame, Avon, магазин пиццы и др.).
🔹 Встроенная корзина и кнопки заказа.

💰 Цена:
🛒 До 10 товаров – 4000 руб.
🛒 До 20 товаров – 7000 руб.
🛒 До 30 товаров – 10000 руб.
🛒 Более 30 товаров – 10000 руб. + 300 руб. за каждый дополнительный товар


📌 Задача: Выгрузка товаров с фото, описанием и фильтрацией по категориям.
💡 Пример использования: Магазин одежды предлагает клиентам выбрать товар прямо в Telegram.
🛠 Техническая реализация:

Пользователь может выбрать категорию, увидеть список товаров, нажать на товар и получить описание.
Хранение данных – SQLite или PostgreSQL.
Бот интегрируется с YooMoney, CloudPayments для приёма платежей.
"""

webinar_tex_double = """🎥 Автовебинарный Бот
📌 Задача: Автоматическая отправка сообщений и видео для прогрева клиентов перед продажей.
💡 Пример использования: Инфобизнесмен продаёт курс, бот отправляет вводный вебинар и после него предложение купить курс.
🛠 Техническая реализация:

Бот регистрирует пользователя, отправляет серию сообщений по таймеру.
Отправка видео/аудио и напоминаний.
Связывается с CRM, где фиксируются данные пользователей.
"""

webinar_text = """🎥 Автовебинарный Бот
🔹 Полноценная автоматизированная воронка продаж с этапами:
✅ Подписка и привлечение клиентов.
✅ Выдача бонусов (чек-листы, консультации).
✅ Прогрев через серию контента.
✅ Вебинар/Мастер-класс + запись эфира.
✅ Дополнительные касания и продажи.

💰 Цена:
🎤 До 15 блоков – 5000 руб.
🎤 До 20 блоков – 7000 руб.
🎤 Более 20 блоков – 7000 руб. + 200 руб. за каждый дополнительный блок


📌 Задача: Автоматическая отправка сообщений и видео для прогрева клиентов перед продажей.
💡 Пример использования: Инфобизнесмен продаёт курс, бот отправляет вводный вебинар и после него предложение купить курс.
🛠 Техническая реализация:

Бот регистрирует пользователя, отправляет серию сообщений по таймеру.
Отправка видео/аудио и напоминаний.
Связывается с CRM, где фиксируются данные пользователей.
"""

shopbot_text_double = """🛒 Чат-бот Магазин
📌 Задача: Полноценный интернет-магазин внутри Telegram с корзиной, оформлением заказа и оплатой.
💡 Пример использования: Доставка суши принимает заказы через бота, пользователи добавляют товары в корзину и оплачивают.
🛠 Техническая реализация:

Пользователь выбирает товары, добавляет в корзину, оформляет заказ.
Оплата через Telegram Pay, Stripe или ЮKassa.
Заказы отправляются менеджеру в CRM, Google Sheets или в телеграмм группу.
"""

shopbot_text = """🛒 Чат-бот Магазин
Название: ShopBot – умный помощник для онлайн-продаж

🔹 Полноценный магазин в формате чат-бота с удобной навигацией и управлением.
🔹 Каталог товаров с описанием, фото и ценами.
🔹 Кнопки "Добавить в корзину", "Оформить заказ", "Подробнее".
🔹 Многоуровневые меню, фильтры и поиск по товарам.
🔹 Подключение платежных систем для онлайн-оплаты.
🔹 Интерактивная админ-панель для управления заказами и клиентами.

💰 Цена:

до 10 товаров – 5000 руб.
до 20 товаров – 8000 руб.
до 30 товаров – 11000 руб.
от 30 товаров – 11000 руб. + 300 руб. за каждый дополнительный товар


📌 Задача: Полноценный интернет-магазин внутри Telegram с корзиной, оформлением заказа и оплатой.
💡 Пример использования: Доставка суши принимает заказы через бота, пользователи добавляют товары в корзину и оплачивают.
🛠 Техническая реализация:

Пользователь выбирает товары, добавляет в корзину, оформляет заказ.
Оплата через Telegram Pay, Stripe или ЮKassa.
Заказы отправляются менеджеру в CRM, Google Sheets или в телеграмм группу.
"""

other_text = """🔧 Другие услуги:
📌 Реконструкция бота – 400 руб./блок
📌 Рассылка с интерактивными кнопками – 700 руб.
"""

popular_types_text_double = """Бот-запись на услуги
📌 Пример: Запись к врачу, мастеру маникюра, фитнес-тренеру.
🛠 Как работает?

Клиент выбирает удобное время из доступных слотов.
Интеграция с Google Calendar или CRM.
"""

popular_types_text = """✍️ Бот-запись на услуги
📌 Пример: Запись к врачу, мастеру маникюра, фитнес-тренеру.
🛠 Как работает?

Клиент выбирает удобное время из доступных слотов.
Интеграция с Google Calendar или CRM.

💰 Цена:
🛒 До 10 товаров – 4000 руб.
🛒 До 20 товаров – 7000 руб.
🛒 До 30 товаров – 10000 руб.
🛒 Более 30 товаров – 10000 руб. + 300 руб. за каждый дополнительный товар
"""

support_service_text = """Бот для службы поддержки
📌 Пример: Подключение FAQ и живых операторов в интернет-магазине.
🛠 Как работает?

Бот отвечает на типичные вопросы (цены, доставка, возврат).
При сложных запросах передаёт клиента оператору.

💰 Цена:

до 10 товаров – 5000 руб.
до 20 товаров – 8000 руб.
до 30 товаров – 11000 руб.
от 30 товаров – 11000 руб. + 300 руб. за каждый дополнительный товар
"""

hr_bot_text_double = """✍️ HR-бот (поиск сотрудников)
📌 Пример: Автоматизация собеседований.
🛠 Как работает?

Кандидат отвечает на вопросы, бот фиксирует данные.
HR получает анкету, приглашает кандидата.
"""

hr_bot_text = """HR-бот (поиск сотрудников)
📌 Пример: Автоматизация собеседований.
🛠 Как работает?

Кандидат отвечает на вопросы, бот фиксирует данные.
HR получает анкету, приглашает кандидата.

💰 Цена:

до 10 товаров – 5000 руб.
до 20 товаров – 8000 руб.
до 30 товаров – 11000 руб.
от 30 товаров – 11000 руб. + 300 руб. за каждый дополнительный товар
"""

selling_text_4 = """❗️ Если Вы не видите кнопку, значит у вас свернуто меню кнопок в телеграм.
Чтобы кнопки отобразились, нажмите на значок ▩ в поле ввода текста 👇🏻
"""

selling_text_44 = """
🔹 Для какой платформы вам нужен чат бот?
🔹 Выберите пункт меню, чтобы продолжить заказ.

❗ Не видите кнопку? Возможно, меню свернуто.
Чтобы отобразить кнопки, просто нажмите на значок ▩, как показано на скриншоте ниже. 👇🏻

Не волнуйтесь, кнопки никуда не делись – они просто прячутся! 😏🚀
"""

selling_text_5 = """Какой функционал и особенности должны быть в боте?
И или выберите нужные пункты в меню👂
"""

selling_text_6 = """Заказ успешно оформлен, в ближайшее время с вами свяжется специалист
"""

selling_text_7 = """"Какая у вас сфера деятельности, и как вы планируете использовать чат-бота? ✍️:
Напишите в поле ввода сообщений и отправьте сообщение"
"""

selling_text_8 = """
Выберите платформу или введите в поле ввода сообщений свой вариант и нажмите кнопку "отправить сообщение"
"""

selling_text_9 = """
Какой функционал и особенности должны быть в вашем боте?
Напишите в поле ввода сообщений и отправьте сообщение
"""

information_inline_menu = """🔹 Inline-меню в Telegram

Так выглядит inline-меню – оно состоит из кнопок, расположенных прямо в сообщении.

✨ Что могут делать кнопки?
🔗 Перенаправлять на сайты, Telegram-каналы и другие ресурсы.
💬 Выводить текстовые сообщения или изображения.
⚙️ Выполнять команды внутри бота.

Нажимай и пробуй! 🚀
"""

information_reply_menu = """🔹 Reply-меню в Telegram

Reply-меню – это кнопки, которые остаются видимыми в поле ввода сообщений.

✨ Что могут делать кнопки?
📌 Отправлять текстовые сообщения.
🖼️ Отправлять изображения.
🔗 Перенаправлять по ссылкам.
🔄 Менять состояние бота и открывать новые разделы.

Выбирай нужную кнопку и управляй ботом легко! 🚀
"""

information_difolt_menu = """🔹 Кнопка меню (три полоски в круге) в Telegram

Эта кнопка открывает дополнительное меню с быстрыми действиями.

✨ Что можно сделать?
📌 Отправить текстовое сообщение.
🖼️ Отправить изображение.
🔗 Перейти по ссылке.
⚙️ Вызвать команды бота.

Используй это меню для удобного взаимодействия с ботом! 🚀
"""

sample_text = """✨ Ваш бот – ваш личный помощник!

Нажатием одной кнопки клиент получает нужную информацию, оформляет заказ или переходит по ссылке.

🔹 Хотите так же? Создадим для вас бота с идеальным текстом и удобными кнопками!

🚀 Давайте сделаем ваш бизнес удобнее уже сегодня!
"""

sample_image_text = """🔹 Изображения в Telegram-боте

Боты могут отправлять не только текст, но и изображения! 📸

✨ Для чего можно использовать картинки? 🛍️ Демонстрация товаров и услуг. 📊 Инфографика и схемы для наглядности. 🎨 Иллюстрации и креативный контент. 📜 Документы и скриншоты.

Добавляйте визуальный контент и сделайте вашего бота еще удобнее! 🚀"
"""

sample_url_text = """🔹 Ссылки в Telegram-боте

Боты могут отправлять не только текст и изображения, но и ссылки! 🔗

✨ Как можно использовать ссылки?
🌍 Перенаправлять пользователей на сайты и магазины.
📢 Вести на Telegram-каналы и чаты.
🎓 Открывать обучающие материалы и статьи.
🛒 Отправлять клиентов в каталоги и формы заказа.

Попробуй прямо сейчас!
Жми на кнопку "🔗 Перейти в группу" 👇
"""

payment_options_text = """🔹 Оплата и процесс работы
Оплата за разработку чат-бота производится в два этапа:
✅ Предоплата 50% – после обсуждения всех деталей заказа.
✅ Оставшиеся 50% – после завершения работы, тестирования и вашего подтверждения.

💳 Доступные способы оплаты:
🔹 Перевод на Сбербанк (по реквизитам).

🚀 Как проходит заказ:
1️⃣ Выбираете нужный тип чат-бота и оформляете заказ.
2️⃣ Я изучаю ваш запрос и связываюсь с вами удобным способом.
3️⃣ Мы обсуждаем все нюансы проекта, уточняем детали.
4️⃣ Вы вносите предоплату 50%.
5️⃣ Я разрабатываю чат-бота, тестирую его и предоставляю вам на проверку.
6️⃣ Если всё устраивает – вы вносите оставшиеся 50% оплаты.
7️⃣ Готовый бот передаётся вам: доступы, инструкция по использованию и поддержка на старте.

📌 Если у вас остались вопросы – напишите мне, и я помогу разобраться! 💬
"""

welcome_text = """Добро пожаловать! 🤖

Вы находитесь в разработанном мною чат-боте, который поможет вам создать собственного бота для бизнеса, автоматизации и многого другого.

🔹 Что умеет бот?
✅ Консультировать клиентов 24/7
✅ Обрабатывать заказы и заявки
✅ Отвечать на частые вопросы
✅ Интегрироваться с CRM и другими сервисами
"""

welcome_text_2 = """👋 Добро пожаловать! Этот бот — ваш личный гид в мире автоматизации продаж.

⚡️ Вы увидите, каким может быть ваш собственный бот:
✅ Разные типы меню и кнопок
✅ Возможности автоматизации
✅ Способы взаимодействия с клиентами
"""

payment_text_work = """🛍 Оплата и процесс работы 🛍
Оплата за разработку чат-бота производится в два этапа:
✅ Предоплата 50% – после обсуждения всех деталей заказа.
✅ Оставшиеся 50% – после завершения работы, тестирования и вашего подтверждения.

💳 Доступные способы оплаты:
🔹 Перевод на Сбербанк (по реквизитам).

🚀 Как проходит заказ:
1️⃣ Выбираете нужный тип чат-бота и оформляете заказ.
2️⃣ Я изучаю ваш запрос и связываюсь с вами удобным способом.
3️⃣ Мы обсуждаем все нюансы проекта, уточняем детали.
4️⃣ Вы вносите предоплату 50%.
5️⃣ Я разрабатываю чат-бота, тестирую его и предоставляю вам на проверку.
6️⃣ Если всё устраивает – вы вносите оставшиеся 50% оплаты.
7️⃣ Готовый бот передаётся вам: доступы, инструкция по использованию и поддержка на старте.

📌 Если у вас остались вопросы – напишите мне, и я помогу разобраться! 💬
"""
