from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# TOKEN - это ключ для доступа к боту, который вы получили от @BotFather
BOT_TOKEN = "5998122265:AAEn61mFFgo1ribFLaILALJlzcvEgS71Nm4"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Конструкция await позволяет получить результат функции, при этом не блокируя выполнение всей программы

    update - объект, который содержит информацию о действии пользователя в боте
    context - объект, который содержит информацию о боте, в котором происходит действие

    effective_chat - конструкция позволяющая получить чат и информацию о нем при произвольном действии (новое сообщение, редактирование сообщения и т.д.)
    """
    await update.effective_chat.send_message(text="Привет! Я бот :)")


if __name__ == "__main__":
    # Создаем объект приложения с ключом доступа к боту
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start_command))

    # Запускаем приложение
    application.run_polling()
