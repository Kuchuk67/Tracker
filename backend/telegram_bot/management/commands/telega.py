from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from django.core.management.base import BaseCommand
from users.models import CustomUser
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from channels.db import database_sync_to_async
from channels.db import database_sync_to_async

class Command(BaseCommand):


    def button_bot(self, update):

        keyboard = [
            [InlineKeyboardButton("Задачи на сегодня", callback_data='1'),
             InlineKeyboardButton("Задачи на завтра", callback_data='2')],
            [InlineKeyboardButton("TOP возможных задач", callback_data='3')],
        ]
        return InlineKeyboardMarkup(keyboard)


    
    @database_sync_to_async
    def add_id_chat(self, update):
        user = CustomUser.objects.get(nick_telegram=update.effective_chat.username)
        user.chat_id_telegram = update.effective_chat.id
        user.save()
        return user

    def handle(self, *args, **kwargs):


        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):



            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="Привет! Я бот трекер-сарвиса 'Атомарные привычки'!"
                                           )
            print("*********", update.effective_chat.username)
            # Тут надо найти в БД пользователя с ником телеграма

            try:
                user = await self.add_id_chat(update)
            except Exception as e:
                print("=====", e)

                # НЕ найдено - пишем что надо зарегится на сервисе
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text="Не найден такой ник. Вам надо зарегится на сервисе "
                                                    "и указать в профиле свой ник в телеге",
                                               #reply_markup=keyboard
                                               )
            else:
                # найдено - записываем туда chat_id и пишем - ок

                
                await update.message.reply_text(
                    'Пожалуйста, выберите:', 
                    reply_markup=self.button_bot(update)
                    )

        async def button(update, _):
            query = update.callback_query
            variant = query.data
            # `CallbackQueries` требует ответа, даже если
            # уведомление для пользователя не требуется, в противном
            #  случае у некоторых клиентов могут возникнуть проблемы.
            # смотри https://core.telegram.org/bots/api#callbackquery.
            await query.answer()

            # редактируем сообщение, тем самым кнопки
            # в чате заменятся на этот ответ.
            await query.edit_message_text(text=f"Выбранный вариант: {variant}")

        # Токен телеграма
        application = ApplicationBuilder().token('7507147736:AAEOYdf3erBfJ-x7unESp431YfAgufAAQ50').build()
        # Добавить обработчик /start
        start_handler = CommandHandler('start', start)
        application.add_handler(start_handler)
        # Добавить обработчик  нажатия кнопки
        application.add_handler(CallbackQueryHandler(button))
        # Зацикливание
        application.run_polling()

