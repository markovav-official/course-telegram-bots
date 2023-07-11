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
    answer = "Твоё сообщение: " + update.message.text

    await update.effective_chat.send_message(text=answer)


if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT, messages_handler))

    application.run_polling()
