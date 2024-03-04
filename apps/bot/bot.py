# ваш код телеграм-бота
import os
import dotenv
import telebot
from telebot import types
from django.core.validators import validate_email

from apps.authorization.models import User
from .utils import valid_email

dotenv.load_dotenv()

# Ваш токен бота
bot_token = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(bot_token)

# Словарь для хранения данных пользователя в контексте
user_data = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой тестовый бот.")

    bot.send_message(message.chat.id, "Для регистрации нажми /register")
@bot.message_handler(commands=['users'])
def get_users(message):
    users = User.objects.all()
    for user in users:
        bot.send_message(message.chat.id, f'ID: {user.id}, Имя: {user.username}, Email: {user.email}, Телефон: {user.phone_number}, Активен: {user.is_active}, Сотрудник: {user.is_staff}')
    bot.send_message(message.chat.id, f'Количество пользователей: {len(users)}')


@bot.message_handler(commands=['register'])
def register(message):
    if User.objects.filter(telegram_id=message.chat.id).exists():
        bot.send_message(message.chat.id, 'Вы уже Авторизованы!')
        return
    bot.send_message(message.chat.id, 'Введите email пользователя:')
    bot.register_next_step_handler(message, add_email)

def add_email(message):
    email = message.text
    # Сохраняем email в контексте

    if User.objects.filter(email=email).exists():
        bot.send_message(message.chat.id, 'Пользователь с таким именем уже существует. Пожалуйста введите другой email')
        bot.register_next_step_handler(message, add_username)

    try: 
        validate_email(email)
    except:
        bot.send_message(message.chat.id, 'Некорректный email. Пожалуйста, введите корректный email.')
        bot.register_next_step_handler(message, add_email)
        return
    if User.objects.filter(email=email).exists():
        bot.send_message(message.chat.id, 'Пользователь с таким email уже существует. Пожалуйста, введите другой email.')
        bot.register_next_step_handler(message, add_email)
        return

    user_data['email'] = email
    bot.send_message(message.chat.id, 'Введите имя пользователя:')
    bot.register_next_step_handler(message, add_username)

def add_username(message):
    username = message.text
    # Получаем email из контекста
    email = user_data.get('email', None)
    
    if email:
        # Создайте экземпляр пользователя и сохраните его
        user = User.objects.create(email=email, username=username, telegram_id=message.chat.id)
        bot.send_message(message.chat.id, f'Пользователь {user.username} успешно добавлен.')
        bot.send_message(message.chat.id, 'Для продолжения выберите действие:', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_users)
    else:
        bot.send_message(message.chat.id, 'Что-то пошло не так. Пожалуйста, попробуйте снова.')

@bot.message_handler(commands=['delete'])
def delete_user(message):
    if not User.objects.filter(telegram_id=message.chat.id).exists():
        bot.send_message(message.chat.id, 'Вы не авторизованы!')
        return
    User.objects.get(telegram_id=message.chat.id).delete()
    bot.send_message(message.chat.id, 'Вы успешно удалили аккаунт для обраной регистрации нажмите на: /register')


def main():
    try:
        print('Бот запущен: https://t.me/Anchik87_bot')
        bot.polling(none_stop=True)
    except
