
# Wallet App

Данное приложение базовый функционал кошелька с пользовательским интерфейсов в Телеграм-боте. У каждого пользователя может быть несколько кошельков одинаковой валюты.
Валюты можно удалять/добавлять через БД.

- Бот хранит курс валюты к USDT ~~и обновляет его через публичное апи~~
- Бот имеет апи для отправки сообщения всем пользователям
- Бот может возвращать по кошельку валюту
- Бот может отдавать список своих кошельков, а так же баланс каждого

Стек: `aiogram3` + `sqlalchemy` + `alembic` + `fastapi` + `pydantic`. Бд: `PostgreSQL`. ~~Docker~~



## Installation
    Python3.12 required

    1. Клонируем репозиторий
    git clone https://github.com/arud3nko/wallet_app.git

    2. Устанавливаем зависимости в virtualenv
    pip install -r requirements.txt

    3. Устанавливаем миграции alembic
    alembic upgrade head

    4. Запускаем скрипт с дефолтными параметрами
    python main.py
    
Тут стоит не забыть, что есть файлики `bot.env` & `db.env`, в них нужно прописать параметры

```
TOKEN=
```

```
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```

Так как я еще не обернул это всё в докер, база (даже пустая) с именем `DB_NAME` должна присутствовать в `posgres`


## Running tests

Можно запустить тесты для пакета `wallet`

    pytest tests
## Packages

### `api`
Пакет `api` предоставляет доступ к API бота (в качестве демонстрации реализован GET-метод для уведомления всех пользователей)

### `bot`

Пакет `bot` предоставляет пользовательский интерфейс wallet_app в TG-боте

`bot.callbacks` - Обработчики CallbackQuery

`bot.filters` - Фильтры для рутинга

`bot.handlers` - Обработчики апдейтов типа Message, конкретная реализация транзакций

`bot.keyboards` - Набор фабрик, создающих клавиатуры

`bot.middlewares` - Набор мидлварей: `ResourcesMiddleware` пробрасывает необходимые ресурсы, `UserMiddleware` пробрасывает инстанс пользователя из БД

`bot.templates` - Набор шаблонов Jinja2 в формате .html

`bot.utils` - Дополнительные утилиты бота. Содержит функцию массовой рассылки

### `db`

В пакете `db` реализована логика работы с базой данных, используя ORM SQLAlchemy и миграции alembic.

`db.exceptions` - Исключения при работе с БД

`db.migrations` - alembic migrations

`db.models` - sa модели

`service` - Сервисы для работы с таблицами

### `wallet`

Пакет `wallet` описывает логику работы кошелька. Здесь лежит `WalletHandler` - фасад, помогающий удобно работать с пакетом. `TransactionHandler` помогает обрабатывать мидлвари для транзакций

`wallet.core` - Pydantic модели

`wallet.exceptions` - Исключения транзакций

`wallet.transactions` - Набор конкретных транзакций, можно сделать какую угодно, имплементирующую все методы базового класса TransactionHandler

`wallet.types` - Типы `Transaction` и `TransactionMiddleware`




