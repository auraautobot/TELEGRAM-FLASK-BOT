import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

# Telegram join request handler
async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()

# Telegram Bot run function
async def run_bot():
    app_ = ApplicationBuilder().token(BOT_TOKEN).build()
    app_.add_handler(ChatJoinRequestHandler(handle_join_request))
    await app_.initialize()
    await app_.start()
    print("Bot started!")

# Thread wrapper
def start_bot_thread():
    import asyncio
    asyncio.run(run_bot())

@app.route('/')
def home():
    return "Flask app and Telegram bot are running."

if __name__ == "__main__":
    threading.Thread(target=start_bot_thread).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
