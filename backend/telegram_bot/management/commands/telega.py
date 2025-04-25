from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from django.core.management.base import BaseCommand
from users.models import CustomUser



class Command(BaseCommand):
  def handle(self, *args, **kwargs):
        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="Привет! Я бот трекер-сарвиса 'Атомарные привычки'!")
            #print(update.effective_chat.username)
            # Тут надо найти в БД пользователя с ником телеграма
            try:
                user = CustomUser.objects.get(nick_telegram=update.effective_chat.username)
            except:
                # НЕ найдено - пишем что надо зарегится на сервисе
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text="Не найден такой ник. Вам надо зарегится на сервисе "
                                                    "и указать в профиле свой ник в телеге"
                                               )
            else:
                # найдено - записываем туда chat_id и пишем - ок
                user.chat_id_telegram = update.effective_chat.id
                user.save()


        application = ApplicationBuilder().token('7507147736:AAEOYdf3erBfJ-x7unESp431YfAgufAAQ50').build()

        start_handler = CommandHandler('start', start)
        application.add_handler(start_handler)

        application.run_polling()