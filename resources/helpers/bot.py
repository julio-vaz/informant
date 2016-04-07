import os
import telepot


def send_message(message):
    try:
        bot = telepot.Bot(os.getenv("INFORMER_BOT_TOKEN"))
        return bot.sendMessage(os.getenv("TELEGRAM_USER_ID"), message)
    except Exception:
        return False
