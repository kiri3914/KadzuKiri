from .settings import bot, bot_token

from .auth import *
from .buttons.categories import *
from .buttons.products import *
from .buttons.carts import *
from .buttons.addresses import *


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой тестовый бот.")
    bot.send_message(message.chat.id, "Для регистрации нажми /register")



def main():
    try:
        print("Бот запущен: https://t.me/asik_king_bot")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")