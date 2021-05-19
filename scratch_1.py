import telebot
bot = telebot.TeleBot('1863921054:AAGbD8-zLX5xDPfMno1d2JY8b-58a3-c1xk')
@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
bot.polling()
