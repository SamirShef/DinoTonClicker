import client
import telebot

bot = telebot.TeleBot(client.TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправляем стикер
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAKnLWZwTe1XxbwDhMZbneoCHb_Rs_rUAAJ6AAMQIQIQAALHI6TJuQU1BA')
    
    # Отправляем текстовое сообщение
    bot.send_message(message.chat.id, 'Приветствую, искатель доисторических богатств! 🦖

Добро пожаловать в мир Dino, где величие динозавров возвращается, чтобы править вновь. Я твой личный гид по этому захватывающему миру, и я здесь, чтобы помочь тебе на пути к несусветным богатствам.

Просто начни кликать, получай монеты и бонусы, и следи за новостями о нашем будущем токене. Если у тебя есть вопросы или тебе нужна помощь, не стесняйся обращаться ко мне.

Вперед, в доисторическое приключение! 🌟')

# Запускаем бота
bot.polling()
