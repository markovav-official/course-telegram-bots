from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

KEYBOARD = [
    [
        InlineKeyboardButton(text="Расписание занятий", callback_data="schedule"),
        InlineKeyboardButton(text="О курсе", callback_data="course_info"),
    ],
    [InlineKeyboardButton(text="Контакты", callback_data="contacts")],
]


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_chat.send_message(
        text="Привет! Я бот. Можешь узнать у меня полезную информацию о курсе",
        reply_markup=InlineKeyboardMarkup(KEYBOARD),
    )


async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    action = update.callback_query.data

    await update.callback_query.answer()

    match action:
        case "schedule":
            await update.effective_chat.send_photo(
                caption="Текущее расписание занятий", photo="static/schedule.png"
            )
        case "course_info":
            await update.effective_chat.send_document(
                caption="Учебный план курса", document="static/syllabus.txt"
            )
        case "contacts":
            await update.effective_chat.send_message(
                text="Контакты преподавателей\nAndrei Markov @markovav_official"
            )


if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(callback_handler))

    application.run_polling()
