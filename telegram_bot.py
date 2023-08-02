import config
import telebot
from model.components import predict, read_imagefile


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Welcome to Neural Network Bot!\n"
                 "Send me an image and I will classify it for you.\n"
                 "Now I can recognize such classes as:"
                 " Airplane, automobile, bird, cat, deer, dog, frog, horse, ship and truck"
                 )


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        # Отримуємо ідентифікатор фото з повідомлення
        photo_id = message.photo[-1].file_id
        # Отримуємо інформацію про фото
        file_info = bot.get_file(photo_id)
        # Завантажуємо фото за посиланням
        downloaded_file = bot.download_file(file_info.file_path)
        # Класифікуємо зображення
        prediction = predict(read_imagefile(downloaded_file))
        # Відправляємо результат класифікації користувачу
        bot.reply_to(message, f"{prediction}")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

if __name__ == '__main__':
    bot.polling()
