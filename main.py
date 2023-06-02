import telebot
from config import BOT_TOKEN
from iaps import analyze
token=BOT_TOKEN
bot=telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я - бот модератор фото. Пришли фотографию и я проанализирую её')

@bot.message_handler(content_types=["photo"])
def emo_analyze(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
        try:
            res = analyze("image.jpg")
        except Exception:
            res = 'Ошибка'
    if res.startswith('Positive'):
        bot.send_message(message.chat.id, 'Милая картинка) Продолжай в том же духе')
    elif res.startswith('Negative'):
        bot.send_message(message.chat.id, 'Картинка содержит неблагоприятный контент')
    else:
        bot.send_message(message.chat.id, 'Картинка нейтральна')

if __name__ == '__main__':
    bot.infinity_polling()