import logging
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
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

from config.states import MAIN_MENU

from config.config import WEBHOOK_URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("магазин", web_app=WebAppInfo(f'{WEBHOOK_URL}/app'))],
        [InlineKeyboardButton("ии помошник", callback_data="ai")],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="привет",reply_markup=markup
    )
    return MAIN_MENU