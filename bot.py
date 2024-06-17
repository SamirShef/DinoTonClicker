import client
import telebot
from telebot import types

bot = telebot.TeleBot(client.TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправляем стикер
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAKnLWZwTe1XxbwDhMZbneoCHb_Rs_rUAAJ6AAMQIQIQAALHI6TJuQU1BA')
    
    # Отправляем текстовое сообщение
    markup = types.InlineKeyboardMarkup()
    play_button = types.InlineKeyboardButton(text="Играть", callback_data="play")
    markup.add(play_button)
    bot.send_message(message.chat.id, 'Приветственное сообщение для пользователя', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "play":
        # Отправляем невидимую команду /game
        bot.send_message(call.message.chat.id, '/game')
        # Здесь можно добавить дополнительные действия, например, запуск игры

# Запускаем бота
bot.polling()