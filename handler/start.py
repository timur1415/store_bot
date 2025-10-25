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
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("магазин", web_app=WebAppInfo(f"{WEBHOOK_URL}/app"))],
        [InlineKeyboardButton("ии помошник", callback_data="ai")],
        [InlineKeyboardButton("поддержка", url="https://t.me/i1i1i1iij")],
        [InlineKeyboardButton("история бренда", callback_data="history")],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    if query:
        query.answer()
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("photo/main_menu.png", "rb"),
            reply_markup=markup,
        )
    else:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("photo/main_menu.png", "rb"),
            reply_markup=markup,
        )
        return MAIN_MENU
