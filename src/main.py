#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from config import API_TOKEN


bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    first_text = f'Hi, {message.from_user.username}'
    bot.reply_to(message, first_text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = message.text
    word_count = len(text.split())
    sumbol_count = len(text)
    answer = f"In your message {word_count} words and {sumbol_count} sumbols"
    bot.reply_to(message, answer)


bot.infinity_polling()