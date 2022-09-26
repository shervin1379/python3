from pytube import YouTube
from telebot import *

bot = TeleBot(token="5629578604:AAHPInmGws51zmycjSf1l13kN3NwbI3cFfA")

@bot.message_handler(["start"])
def start(message):
   markup=types.ReplyKeyboardMarkup()
   music=types.KeyboardButton("Music")
   markup.add(music)
   bot.send_message(message.chat.id, "text",reply_markup=markup)

if __name__=="__main__":
   bot.infinity_polling(timeout=20)
