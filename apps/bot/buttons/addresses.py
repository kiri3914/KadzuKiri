from telebot import types
from nominatim import NominatimReverse  # pip install nominatim 

from apps.bot.settings import bot
from apps.customers.models import Adress, Client

def get_address(latitude, longitude):
    """
    Получение адреса по координатам
    # Инициализация геокодера
    # geolocator = NominatimReverse()
    #
    # # Координаты 43.25685,76.93281
    # latitude = 43.25790
    # longitude = 76.93281
    #
    # # Получение адреса
    # address = geolocator.query(latitude, longitude)
    """
    geolocator = NominatimReverse()
    address = geolocator.query(latitude, longitude)
    return address['address']


@bot.message_handler(commands=['address'])
def address(message):
    """
    Отправка клавиатуры с кнопкой для получения координат места находения
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton(
            text='Отправить место находение', 
            request_location=True)  # request_location=True для получения координат места находения
        )

    bot.send_message(
        message.chat.id,
        'Отправьте место находение',
        reply_markup=markup)

    bot.register_next_step_handler(message, address_handler)  # Регистрация обработчика для координат места находения


def address_handler(message):
    """
    Обработчик для координат места находения
    """
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        address = get_address(latitude, longitude)
        if address:
            instance = create_address(message.chat.id, address)
            if instance:
                bot.send_message(message.chat.id, 'Адрес успешно создан')
                bot.send_message(message.chat.id, instance)
            else:
                bot.send_message(message.chat.id, 'Вы не авторизованы')   
    else:
        bot.send_message(message.chat.id, 'Не удалось получить адрес')



def create_address(tg_id, address):
    """
    Создание адреса
    """
    client =  Client.objects.filter(user__telegram_id=tg_id)
    if client:
        customer = client.first()
        city = address['city']
        street = address['road']
        home = address['house_number']
        address = Adress.objects.create(
            customer=customer,
            city=city,
            street=street,
            home=home
            )
        return address
    




# # Инициализация геокодера
# geolocator = NominatimReverse()

# # Координаты 43.25685,76.93281
# latitude = 43.25790
# longitude = 76.93281

# # Получение адреса
# address = geolocator.query(latitude, longitude)

# # Печать адреса
# from pprint import pprint

# pprint(address['address'])
