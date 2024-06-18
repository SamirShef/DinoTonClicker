import client
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

STICKER_ID = 'CAACAgIAAxkBAAKnLWZwTe1XxbwDhMZbneoCHb_Rs_rUAAJ6AAMQIQIQAALHI6TJuQU1BA'
GAME_URL = 'https://samirshef.github.io/DinoTonClicker/'

bot = Bot(client.TOKEN)
updater = Updater(bot=bot, use_context=True)
def start(update, context):
    # Отправляем стикер
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=STICKER_ID)
    
    # Отправляем приветственное сообщение
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Добро пожаловать в игру.")

    # Создаем кнопку "Играть"
    keyboard = [[InlineKeyboardButton("Играть", callback_data='play')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем сообщение с кнопкой
    context.bot.send_message(chat_id=update.effective_chat.id, text="Нажмите кнопку ниже, чтобы начать играть!", reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    
    # Проверяем callback_data и открываем игру
    if query.data == 'play':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Открываю игру...", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Играть", url=GAME_URL)]]))

# Добавляем обработчики команд
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

# Запускаем бота
updater.start_polling()
updater.idle()