from apps.bot.services.carts import cart_service
from apps.bot.settings import bot
from telebot import types


# Купить продукт
@bot.callback_query_handler(func=lambda call: call.data.startswith('buy_'))
def add_product_cart(call):
    """
    Если нажата кнопка купить, берем айди товара 
    Достаем корзину по телеграмм айди
    И добавляем продукт в корзину
    """
    product_id = int(call.data.split('_')[1])
    tg_id = call.from_user.id
    cart = cart_service.get_cart(tg_id)
    cart_item = cart_service.add_product(cart, product_id, 1)
    if cart_item:
        bot.send_message(call.from_user.id, 'Товар добавлен в корзину, чтобы посмотреть корзину нажмите /cart')
        bot.delete_message(call.message.chat.id,  call.message.message_id) # Удаляем сообщение
        return
    bot.send_message(call.from_user.id, 'Не удалось добавить товар в корзину')
    
    
    
@bot.message_handler(commands=['cart'])
def show_cart(message):
    """
    Выводим корзину
    """
    tg_id = message.from_user.id
    cart = cart_service.get_cart(tg_id)
    if cart:
        items = cart_service.get_cart_items(cart)
        markup = types.InlineKeyboardMarkup()
        for item in items:
            markup.add(types.InlineKeyboardButton(text=item.product.name, callback_data=f'cartitem_{item.product.id}'))
        bot.send_message(message.chat.id, 'Ваши товары: ', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Корзина пуста')
        bot.delete_message(message.chat.id, message.message_id) # Удаляем сообщение
        return
    
    

@bot.callback_query_handler(func=lambda call: call.data.startswith('cartitem_'))
def show_cart_item(call):
    """
    Показываем информацию о товаре
    """
    product_id = int(call.data.split('_')[1])
    tg_id = call.from_user.id
    cart = cart_service.get_cart(tg_id)
    cart_item = cart_service.get_cart_item_by_product(cart ,product_id)
    bot.delete_message(call.message.chat.id, call.message.message_id) # Удаляем сообщение
    
    product = cart_item.product
    text = f'Название: {product.name}\n'\
           f'Цена: {product.price} тенге.\n'\
           f'Описание: {product.description}\n'\
           f'Дата публикации: {product.created_at}\n'\
           f"В наличии: {'Есть' if product.is_available else 'Нет'}\n"\
           f"Количество: {cart_item.count}\n"\
           f"Итого: {cart_item.total_price}\n"\
               
    # Создаем клавиатуру для удаления товара из корзины
    markup = types.InlineKeyboardMarkup()    
    markup.add(
        types.InlineKeyboardButton(text='Удалить', callback_data=f'deletecartitem_{cart_item.id}')
        )
    markup.add(
        types.InlineKeyboardButton(text='+', callback_data=f'increasecartitem_{cart_item.id}')
        )    
    markup.add(
        types.InlineKeyboardButton(text='-', callback_data=f'decreaseecartitem_{cart_item.id}')
        )   
    
    with open(product.base_image.path, 'rb') as image:
        bot.send_photo(call.message.chat.id, image, caption=text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('deletecartitem_'))
def delete_cart_item(call):
    """
    Удаляем товар из корзины
    """
    cart_item_id = int(call.data.split('_')[1])
    cart_item = cart_service.get_cart_item(cart_item_id)
    cart_service.delete_cart_item(cart_item)
    bot.send_message(call.message.chat.id, 'Товар удален из корзины, Нажмите чтобы посмотреть Корзину /cart')
    bot.delete_message(call.message.chat.id, call.message.message_id) # Удаляем сообщение
    
    
    
@bot.callback_query_handler(func=lambda call: call.data.startswith('increasecartitem_'))
def increase_cart_item(call):
    """
    Увеличиваем количество товара в корзине
    """
    cart_item_id = int(call.data.split('_')[1])
    cart_item = cart_service.get_cart_item(cart_item_id)
    cart_service.increment(cart_item)
    
    bot.delete_message(call.message.chat.id, call.message.message_id) # Удаляем сообщение
 
    product = cart_item.product
    text = f'Название: {product.name}\n'\
           f'Цена: {product.price} тенге.\n'\
           f'Описание: {product.description}\n'\
           f'Дата публикации: {product.created_at}\n'\
           f"В наличии: {'Есть' if product.is_available else 'Нет'}\n"\
           f"Количество: {cart_item.count}\n"\
           f"Итого: {cart_item.total_price}\n"\
               
    # Создаем клавиатуру для удаления товара из корзины
    markup = types.InlineKeyboardMarkup()    
    markup.add(
        types.InlineKeyboardButton(text='Удалить', callback_data=f'deletecartitem_{cart_item.id}')
        )
    markup.add(
        types.InlineKeyboardButton(text='+', callback_data=f'increasecartitem_{cart_item.id}')
        )    
    markup.add(
        types.InlineKeyboardButton(text='-', callback_data=f'decreaseecartitem_{cart_item.id}')
        )   
    
    with open(product.base_image.path, 'rb') as image:
        bot.send_photo(call.message.chat.id, image, caption=text, reply_markup=markup)

    
    
    
@bot.callback_query_handler(func=lambda call: call.data.startswith('decreaseecartitem_'))
def decrease_cart_item(call):
    """
    Уменьшаем количество товара в корзине
    """
    cart_item_id = int(call.data.split('_')[1])
    cart_item = cart_service.get_cart_item(cart_item_id)
    cart_service.decrement(cart_item)
    bot.delete_message(call.message.chat.id, call.message.message_id) # Удаляем сообщение

    product = cart_item.product
    text = f'Название: {product.name}\n'\
           f'Цена: {product.price} тенге.\n'\
           f'Описание: {product.description}\n'\
           f'Дата публикации: {product.created_at}\n'\
           f"В наличии: {'Есть' if product.is_available else 'Нет'}\n"\
           f"Количество: {cart_item.count}\n"\
           f"Итого: {cart_item.total_price}\n"\
               
    # Создаем клавиатуру для удаления товара из корзины
    markup = types.InlineKeyboardMarkup()    
    markup.add(
        types.InlineKeyboardButton(text='Удалить', callback_data=f'deletecartitem_{cart_item.id}')
        )
    markup.add(
        types.InlineKeyboardButton(text='+', callback_data=f'increasecartitem_{cart_item.id}')
        )    
    markup.add(
        types.InlineKeyboardButton(text='-', callback_data=f'decreaseecartitem_{cart_item.id}')
        )   
    
    with open(product.base_image.path, 'rb') as image:
        bot.send_photo(call.message.chat.id, image, caption=text, reply_markup=markup)

