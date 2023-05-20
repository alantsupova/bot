import telebot
from telebot import types
from config import BOT_TOKEN
from emtion_detection import face_analize
import requests
token=BOT_TOKEN
bot=telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я - бот для анализа эмоционального окраса фото. Пришли фотографию и я проанализирую её')

@bot.message_handler(content_types=["photo"])
def emo_analyze(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
        try:
            res = face_analize("image.jpg")
        except Exception:
            res = 'Лицо не распознано'
    bot.send_message(message.chat.id, res)

if __name__ == '__main__':
    bot.infinity_polling()