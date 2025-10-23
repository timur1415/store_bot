import logging
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
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

from config.config import GPT_TOKEN

from config.states import AI

from openai import AsyncOpenAI


async def ai_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=" Привет! Это наш ии ассистент. задай любой вопрос и он ответит на него!",
    )
    return AI


async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["questions"] = update.effective_message.text
    client = AsyncOpenAI(api_key=GPT_TOKEN)
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]
    markup = InlineKeyboardMarkup(keyboard)

    response = await client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "developer",
                "content": "ты ии помощник в магазине ПоймайКа tore и ты отвечаешь на абсолютно все вопросы которые тебе задают, максимально позитивно и радостно. ты должен отвечать очень максимально правильно в плане грамматики и красиво в плане стилистики",
            },
            {"role": "user", "content": context.user_data["questions"]},
        ],
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=response.output_text, reply_markup=markup
    )