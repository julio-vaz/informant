import os
import telepot


def send_message(user_id, message):
    try:
        bot = telepot.Bot(os.getenv("INFORMER_BOT_TOKEN"))
        return bot.sendMessage(user_id, message)
    except Exception:
        return False
