from telebot import types
from apps.bot.services.categories import category_service

from apps.bot.settings import bot

def get_categories_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    categories = category_service.get_categories()
    for category in categories:
        keyboard.add(types.InlineKeyboardButton(
                                text=category.title, 
                                callback_data=f"category_{category.id}"))
    return keyboard


@bot.message_handler(commands=['categories'])
def categories(message):
    bot.send_message(message.chat.id, "Выберите категорию:", 
                    reply_markup=get_categories_keyboard())
    return

