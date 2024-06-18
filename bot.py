import client
import telebot
from telebot import types

bot = telebot.TeleBot(client.TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправляем стикер
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAKnLWZwTe1XxbwDhMZbneoCHb_Rs_rUAAJ6AAMQIQIQAALHI6TJuQU1BA')
    
    # Отправляем текстовое сообщение
    markup = telebot.types.InlineKeyboardMarkup()
    play_button = types.InlineKeyboardButton(text="Играт", callback_data="play")
    markup.add(play_button)
    bot.send_message(message.chat.id, 'даров', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'play':
        # URL вашей игры на GitHub
        game_url = 'https://samirshef.github.io/DinoTonClicker/'
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Нажмите здесь, чтобы начать игру:', reply_markup=types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="Играть", url=game_url)]]))


# Запускаем бота
bot.polling()