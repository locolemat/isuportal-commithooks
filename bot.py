import os

from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()
token = os.getenv('BOT_TOKEN')
commit_chat = os.getenv('COMMIT_CHAT')
bot = TeleBot(token, parse_mode=None)

def send_commit_message(msg, author, repo):
    message = f"Коммит залетел!\nРепозиторий: {repo}\nАвтор: {author}\nСообщение: {msg}"
    bot.send_message(chat_id=commit_chat, text=message)
