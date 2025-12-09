import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
button1_text = "Are you shure?"
button1 = KeyboardButton(text=button1_text)
keyboard.add(button1)

# test changes

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    first_text = f'Hi, {message.from_user.username}'
    bot.send_message(message.from_user.id, first_text, reply_markup=keyboard)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = message.text
    if text==button1_text:
        bot.reply_to(message, "NO")#str(message))
        return
    word_count = len(text.split())
    sumbol_count = len(text)
    answer = f"In your message {word_count} words and {sumbol_count} sumbols"
    bot.reply_to(message, answer)


bot.infinity_polling()