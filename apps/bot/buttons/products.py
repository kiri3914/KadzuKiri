from telebot import types
from apps.bot.services.products import product_service

from apps.bot.settings import bot


@bot.callback_query_handler(func=lambda call: call.data.startswith('category_'))
def show_products_by_category(call):
    category_id = int(call.data.split('_')[1])
    bot.delete_message(call.message.chat.id, call.message.message_id)

    products = product_service.get_products_by_category(category_id)
    if products:
        keyboard = types.InlineKeyboardMarkup()
        for product in products:
            keyboard.add(types.InlineKeyboardButton(text=product.name, callback_data=f'product_{product.id}'))
            bot.send_message(call.message.chat.id, 'Выберите товар:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('product_'))
def show_product_info(call):
    product_id = int(call.data.split('_')[1])
    product = product_service.get_product_by_id(product_id)
    bot.delete_message(call.message.chat.id, call.message.message_id)

    text = f'Название: {product.name}\n'\
           f'Цена: {product.price} тенге.\n'\
           f'Описание: {product.description}\n'\
           f'Дата публикации: {product.created_at}\n'\
           f"В наличии: {'Есть' if product.is_available else 'Нет'}"
    with open(product.base_image.path, 'rb') as image:
        if product.is_available:
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text='Купить', 
                                                    callback_data=f'buy_{product.id}'))
            bot.send_photo(call.message.chat.id, image, caption=text, reply_markup=keyboard)
        bot.send_photo(call.message.chat.id, image, caption=text, reply_markup=keyboard)

