from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Я бот, пожалуйста, поговори со мной!")
    print(update.effective_chat.username)
    # Тут надо найти в БД пользователя с ником телеграма
    # найдено - записываем туда chat_id и пишем - ок
    # НЕ найдено - пишем что надо зарегится на сервисе



if __name__ == '__main__':
    application = ApplicationBuilder().token('7507147736:AAEOYdf3erBfJ-x7unESp431YfAgufAAQ50').build()


    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()

