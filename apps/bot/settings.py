import os
import dotenv
import telebot

dotenv.load_dotenv()

bot_token = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(bot_token)