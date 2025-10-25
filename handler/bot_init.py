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
from config.states import MAIN_MENU, AI, HISTORY
from handler.ai import ai_start, ai
from handler.start import start
from handler.history import history


def create_bot_app() -> Application:
    persistence = PicklePersistence(filepath="store_bot")
    telegram_app = ApplicationBuilder().token(TOKEN).persistence(persistence).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAIN_MENU: [
                CallbackQueryHandler(ai_start, pattern="^ai$"),
                CallbackQueryHandler(history, pattern='^history$')
            ],  # noqa: F821
            AI: [MessageHandler(filters.TEXT & ~filters.COMMAND, ai),
                 CallbackQueryHandler(start, 'back')],
            HISTORY:[MessageHandler(filters.TEXT & ~filters.COMMAND, history),
                 CallbackQueryHandler(start, 'exit')]
        },
        name="store_bot",
        persistent=True,
        fallbacks=[CommandHandler("start", start)],
    )

    telegram_app.add_handler(conv_handler)
    return telegram_app
