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

from config.states import HISTORY

from config.config import WEBHOOK_URL


async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("в магазин", web_app=WebAppInfo(f"{WEBHOOK_URL}/app"))],
        [InlineKeyboardButton("выход", callback_data="exit")],
    ]

    markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open("photo/history.jpg", "rb"),
        caption="💜 ПоймайКа — это проект от команды, создающей автоматы с игрушками.\n🧸 Мы решили открыть магазин для тех, кто не смог поймать игрушку, но всё же хочет найти своего плюшевого друга.\n✨ Пока у нас только игрушки, но впереди — многое: одежда, электроника и всё, что делает жизнь уютнее.",
        reply_markup=markup,
    )
    return HISTORY