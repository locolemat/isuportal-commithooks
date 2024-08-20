import os

from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from emoji import emojize

load_dotenv()
token = os.getenv('BOT_TOKEN')
commit_chat = os.getenv('COMMIT_CHAT')
bot = TeleBot(token, parse_mode="HTML")

def generate_commit_url_button(url):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Открыть", url=url))
    return markup

def send_commit_message(msg, author, branch, url):
    message = emojize(f":hammer_and_pick:Коммит залетел!\n<b>Ветка</b>: {branch}\n<b>Автор</b>: {author}\n<b>Сообщение</b>: {msg}\n<b>Ссылка</b>: {url}")
    bot.send_message(chat_id=commit_chat, text=message, reply_markup=generate_commit_url_button(url))
