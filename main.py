import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.environ.get("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("سلام 👋\nبه ربات آموزش زبان انگلیسی خوش آمدی 🇬🇧")

def word(update, context):
    update.message.reply_text("apple = سیب 🍎")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("word", word))

updater.start_polling()
updater.idle()
