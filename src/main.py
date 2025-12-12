import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
button1_text = "Are you shure?"
button1 = KeyboardButton(text=button1_text)
keyboard.add(button1)
state = {}

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    global state
    first_text = f'Hi, {message.from_user.username}'
    bot.send_message(message.from_user.id, first_text, reply_markup=keyboard)
    state[message.from_user.id]={"room":1, "hp":5}

def rooms(text, message):
    global state
    if text == "Налево" and state[message.from_user.id]["room"] == 1:
        bot.send_message(
            message.from_user.id,
            f'Ты пошел налево из комнаты {state[message.from_user.id]["room"]}',
        )
        state[message.from_user.id]["room"]=3
    elif text == "Направо" and state[message.from_user.id]["room"] == 1:
        bot.send_message(
            message.from_user.id,
            f'Ты пошел налево из комнаты {state[message.from_user.id]["room"]}',
            reply_markup=keyboard
        )
        state[message.from_user.id]["room"]=2
    elif (text == "Налево" and state[message.from_user.id]["room"] == 2) or (text == "Направо" and state[message.from_user.id]["room"] == 3):
        bot.send_message(
            message.from_user.id,
            f'Ты пошел налево из комнаты {state[message.from_user.id]["room"]}',
        )
        state[message.from_user.id]["room"]=5
    elif text == "Направо" and state[message.from_user.id]["room"] == 2:
        bot.send_message(
            message.from_user.id,
            f'Ты пошел налево из комнаты {state[message.from_user.id]["room"]}',
            reply_markup=keyboard
        )
        state[message.from_user.id]["room"]=4
    elif text == "Налево" and state[message.from_user.id]["room"] == 3:
        bot.send_message(
            message.from_user.id,
            f'Ты пошел налево из комнаты {state[message.from_user.id]["room"]}',
        )
        state[message.from_user.id]["room"]=6
    if text == "Налево" or text == "Направо":
        return 1
    else:
        return 0

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global state
    text = message.text
    if text==button1_text:
        bot.reply_to(message, "NO")#str(message))
        return
    elif rooms(text, message)==1:
        return
    else:
        word_count = len(text.split())
        sumbol_count = len(text)
        answer = f"In your message {word_count} words and {sumbol_count} sumbols"
        bot.reply_to(message, answer)


bot.infinity_polling()