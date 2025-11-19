import logging
from telegram import Update, Bot
from telegram.ext import (
    Application,
    ApplicationBuilder,
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    CallbackQueryHandler,
    PicklePersistence,
    MessageHandler,
    filters,
)
from config.config import TOKEN
from config.states import MAIN_MENU, AI, HISTORY, REVIEWS_HANDLER, REVIEWS, GET_NAME_REVIEWS
from handler.ai import ai_start, ai
from handler.start import start
from handler.history import history
from handler.reviews_handler import get_reviews, reviews_handler, get_name_reviews, name_reviews


def create_bot_app() -> Application:
    persistence = PicklePersistence(filepath="store_bot")
    telegram_app = ApplicationBuilder().token(TOKEN).persistence(persistence).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAIN_MENU: [
                CallbackQueryHandler(ai_start, pattern="^ai$"),
                CallbackQueryHandler(history, pattern="^history$"),
                CallbackQueryHandler(reviews_handler, pattern="^start_reviews$")
            ],
            AI: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, ai),
                CallbackQueryHandler(start, "back"),
            ],
            HISTORY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, history),
                CallbackQueryHandler(start, "exit"),
            ],
            REVIEWS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, get_reviews),
            ],
            REVIEWS_HANDLER: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, reviews_handler),
                CallbackQueryHandler(name_reviews, pattern="^reviews$"),
            ],
            GET_NAME_REVIEWS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, get_name_reviews),
                CallbackQueryHandler(start, "main_menu")]
        },
        name="store_bot",
        persistent=True,
        fallbacks=[CommandHandler("start", start)],
    )

    telegram_app.add_handler(conv_handler)
    return telegram_app
