from telebot import types
from apps.bot.settings import bot
from apps.bot.services.carts import cart_service



@bot.callback_query_handler(func=lambda call: call.data.startswith('buy_'))
def add_product_cart(call):
    """
    Добавление товара в корзину
    product_id = id продукта переданный в callback_data
    tg_id = id пользователя
    cart = корзина пользователя
    cart_item = продукт корзины
    """
    product_id = int(call.data.split('_')[1])
    tg_id = call.from_user.id
    cart = cart_service.get_cart(tg_id)
    cart_item = cart_service.add_product(cart, product_id, 1)
    if cart_item:
        bot.send_message(call.message.chat.id, 'Товар добавлен в корзину!')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return
    bot.send_message(call.message.chat.id, 'Не удолось добавить товар в корзину!')





@bot.message_handler(commands=['cart'])
def show_cart(message):
    """
    Показать корзину пользователя
    """
    tg_id = message.from_user.id
    cart = cart_service.get_cart(tg_id)
    if cart:
        items = cart_service.get_cart_items(cart)
        markup = types.InlineKeyboardMarkup()
        for item in items:
            markup.add(types.InlineKeyboardButton(
                text=item.product.name,
                callback_data=f'cartitem_{item.product.id}'))
        bot.send_message(message.chat.id, 'Ваши товары: ', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Корзина пуста!')
        bot.delete_message(message.chat.id, message.message_id)
        return

@bot.callback_query_handler(func=lambda call: call.data.startswith('cartitem_'))
def show_cart_item(call):
    """
    Показать товар из корзины
    """
    product_id = int(call.data.split('_')[1])
    tg_id = call.from_user.id
    cart = cart_service.get_cart(tg_id)
    cart_item = cart_service.get_cart_item_by_product(cart, product_id)
    product = cart_item.product
    text = f'Название: {product.name}\n' \
       f'Цена: {product.price}\n' \
       f'Количество: {cart_item.count}\n' \
       f'Итого: {cart_item.total_price}'
    # Создаем клавиатуру для кнопки Удаления и редактирования
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(text='Удалить', callback_data=f'deletecartitem_{cart_item.id}')
    )
    markup.add(
        types.InlineKeyboardButton(text='+', callback_data=f'increasecartitem_{cart_item.id}')
    )
    markup.add(
        types.InlineKeyboardButton(text='-', callback_data=f'decreasecartitem_{cart_item.id}')
    )

    with open(product.base_image.path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=text, reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: call.data.startswith('deletecartitem_'))
def delete_cart_item(call):
    """
    Удалить товар из корзины
    """
    cart_item_id = int(call.data.split('_')[1])
    cart_item = cart_service.get_cart_item(cart_item_id)
    cart_service.delete_cart_item(cart_item_id)
    bot.send_message(call.message.chat.id, 'Товар удален из корзины!')
    bot.delete_message(call.message.chat.id, call.message.message_id)