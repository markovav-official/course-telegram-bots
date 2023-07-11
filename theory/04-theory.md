## **Теория**

### **.env файл или как правильно хранить секреты**

В прошлом задании мы создали бота, который отвечает на команду `/start` сообщением `Привет! Я бот :)`

Но если вы посмотрите на код, то увидите, что токен бота хранится в открытом виде:

```python
BOT_TOKEN = "0123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
```

В реальности такой подход не приведет ни к чему хорошему. 
1. Такой код тяжело поддерживать, так как если захочется поменять токен бота, придется искать его в исходном коде, что неудобно. 
2. Таким кодом нельзя делиться, так как любой человек сможет получить доступ к вашему боту и управлять им.

Поэтому в реальных проектах токен бота хранится в отдельном файле `.env`, который кроме токена может содержать и другие секреты. В нашем случае в файле `.env` будет только токен бота.

```env
BOT_TOKEN=0123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
```
> Это формат файла `.env`, в котором каждая строка имеет вид `ключ=значение` и каждая строка отвечает за один секрет.

Чтобы загрузить токен бота из файла `.env` в код, нужен пакет `python-dotenv` позволяющий импортировать секреты следующим образом:

```python
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
```

## **Эхо-бот**

Эхо-бот - это бот, который повторяет сообщение пользователя. Давайте создадим такого бота.

```python
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_chat.send_message(text="Привет! Я бот :)")


async def messages_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass


if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT, messages_handler))

    application.run_polling()

```


### **Реализация обработчика сообщений**

В функции `messages_handler` нужно отправить сообщение пользователю:

```python
async def messages_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = "Твоё сообщение: " + update.message.text

    await update.effective_chat.send_message(text=answer)
```

### **Запуск бота**

Для запуска бота нужно выполнить команду

```shell
python 04-echo-bot.py
```

После запуска бота, он будет отвечать на команду `/start` сообщением `Привет! Я бот :)`
и на любое сообщение пользователя, повторяя его.

## **Задание:**

- В файле `04-echo-bot.py`

- Добавьте условие, если пользователь отправил слово `Привет`, то бот должен ответить `Привет! Как дела?`, иначе бот должен ответить `Я не понимаю тебя :(`

## Ожидаемый результат:

При запуске команды

```shell
python 04-echo-bot.py
```

Бот должен отвечать на команду `/start` сообщением `Привет! Я бот :)`. \
При отправке сообщения `Привет`, бот должен ответить `Привет! Как дела?`. \
При отправке любого другого сообщения, бот должен ответить `Я не понимаю тебя :(`.