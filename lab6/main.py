import telebot
from telebot import types
import pytz
from datetime import datetime


token = ''

with open('token.txt', 'r') as f:
    token = f.readline()
bot = telebot.TeleBot(token)


moscowTimezone = pytz.timezone("Europe/Moscow")
moscowTime = datetime.now(moscowTimezone)
currentMoscowTime = moscowTime.strftime("%H:%M:%S")

londonTimezone = pytz.timezone("Europe/London")
londonTime = datetime.now(londonTimezone)
currentLondonTime = londonTime.strftime("%H:%M:%S")

newyorkTimezone = pytz.timezone("America/New_York")
newyorkTime = datetime.now(newyorkTimezone)
currentNewyorkTime = newyorkTime.strftime("%H:%M:%S")


@bot.message_handler(commands=["start"])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Москва")
    item2 = types.KeyboardButton("Лондон")
    item3 = types.KeyboardButton("Нью-Йорк")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, '*Выберите город для вывода местного времени:*', parse_mode='MarkdownV2', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Москва':
        bot.send_message(message.chat.id, 'Время в Москве: ' + currentMoscowTime)
    elif message.text.strip() == 'Лондон':
        bot.send_message(message.chat.id, 'Время в Лондоне: ' + currentLondonTime)
    elif message.text.strip() == 'Нью-Йорк':
        bot.send_message(message.chat.id, 'Время в Нью-Йорке: ' + currentNewyorkTime)
    else:
        bot.send_message(message.chat.id, 'Такой команды не существует.')

bot.polling(none_stop=True, interval=0)
