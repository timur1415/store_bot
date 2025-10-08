import logging
from telegram import Update, Bot
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    CallbackQueryHandler,
    PicklePersistence,
    MessageHandler,
    filters,
    
)
async def magaz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="магаз тут будет ок?",
            )