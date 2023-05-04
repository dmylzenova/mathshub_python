import logging
import telebot

# добавим логгирование, чтобы получать сообщения в консоль
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


def run_simple_bot(token: str) -> None:
    """Run simple telegram bot."""
    bot = telebot.TeleBot(token, parse_mode=None)

    # добавим Handler, обрабатывающий команду start
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        """ Respond to a /start message. """
        bot.reply_to(message, "Привет!")

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        """ Respond to text messages. """
        if message.text.lower() == "привет":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши привет")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

    @bot.message_handler(content_types=['photo'])
    def get_image_messages(message):
        """ Responds to receiving photo from user.
        Saves image to disk and sends it back.
        """
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        # сохранить изображение на диск
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)

        # загрузить изображение с диска
        with open('image.jpg', 'rb') as file:
            new_photo = file.read()

        bot.send_photo(message.from_user.id, new_photo)


    # запустим бота
    bot.infinity_polling()


if __name__ == '__main__':
    run_simple_bot("YOUR_TOKEN")