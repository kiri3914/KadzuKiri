from telebot import types
from apps.customers.models import Client, Address
from apps.bot.settings import bot
from apps.bot.services.deliveries import delivery_service

def create_address(message):


@bot.callback_query_handler(func=lambda call: call.data.startwith('order_'))
def order(call: types.CallbackQuery):
    tg_id = call.from_user.id
    addresses = Address.objects.filter(customer__user__telegram_id=tg_id)
    if not addresses:
        


@bot.callback_query_handler(func=lambda call: call.data.startwith('deliverycart_'))
def delivery(call):
    cart_id = int(call.data.split('_')[1])

    delivery_service.create_delivery()