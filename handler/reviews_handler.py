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

from config.states import REVIEWS, REVIEWS_HANDLER

async def reviews_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Посмотреть отзывы", url="https://t.me/rewiews_store")],
        [InlineKeyboardButton("Оставить отзыв", callback_data="reviews")],
    ]

    markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open("photo/main_menu.png", "rb"),
        reply_markup=markup,
    )
    return REVIEWS_HANDLER

async def text_reviews(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    query.answer()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="ждём твой от тебя отзыв что бы все могли увидеть наши заслуги",
    )

    return REVIEWS

async def get_reviews(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['reviews'] = update.effective_message.text
    keyboard = [[InlineKeyboardButton('в главное меню', callback_data='main_menu')]]
    markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="спасибо за отзыв",
        reply_markup=markup
    )