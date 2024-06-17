import client
import telebot

bot = telebot.TeleBot(client.TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправляем стикер
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAKnLWZwTe1XxbwDhMZbneoCHb_Rs_rUAAJ6AAMQIQIQAALHI6TJuQU1BA')
    
    # Отправляем текстовое сообщение
    bot.send_message(message.chat.id, 'Приветственное сообщение для пользователя')

# Запускаем бота
bot.polling()