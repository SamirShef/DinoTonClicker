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
    play_button = types.InlineKeyboardButton(text="Играть", url="https://samirshef.github.io/DinoTonClicker/")
    markup.add(play_button)
    bot.send_message(message.chat.id, 'даров, баран', reply_markup=markup)

# Запускаем бота
bot.polling()