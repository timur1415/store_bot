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
from config.states import MAIN_MENU, MAGAZ, AI
from handler.ai import ai_start, ai
from handler.magaz import magaz
from handler.start import start


def create_bot_app() -> Application:
    persistence = PicklePersistence(filepath="store_bot")
    telegram_app = ApplicationBuilder().token(TOKEN).persistence(persistence).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAIN_MENU: [
                CallbackQueryHandler(magaz, "magaz"),
                CallbackQueryHandler(ai_start, "ai"),
            ],  # noqa: F821
            AI: [MessageHandler(filters.TEXT & ~filters.COMMAND, ai)],
            MAGAZ: [CallbackQueryHandler(magaz)],
        },
        name="store_bot",
        persistent=True,
        fallbacks=[CommandHandler("start", start)],
    )

    telegram_app.add_handler(conv_handler)
    return telegram_app
