from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from django.core.management.base import BaseCommand
from users.models import CustomUser
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


class Command(BaseCommand):


    def button_bot(self, update):

        keyboard = [
            [InlineKeyboardButton("Задачи на сегодня", callback_data='1'),
             InlineKeyboardButton("Задачи на завтра", callback_data='2')],
            [InlineKeyboardButton("TOP возможных задач", callback_data='3')],
        ]
        return InlineKeyboardMarkup(keyboard)



    def handle(self, *args, **kwargs):
        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):



            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="Привет! Я бот трекер-сарвиса 'Атомарные привычки'!"
                                           )

            # Тут надо найти в БД пользователя с ником телеграма
            try:
                user = CustomUser.objects.get(nick_telegram=update.effective_chat.username)
            except:
                # НЕ найдено - пишем что надо зарегится на сервисе
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text="Не найден такой ник. Вам надо зарегится на сервисе "
                                                    "и указать в профиле свой ник в телеге",
                                               #reply_markup=keyboard
                                               )
            else:
                # найдено - записываем туда chat_id и пишем - ок
                user.chat_id_telegram = update.effective_chat.id
                user.save()
                await update.message.reply_text('Пожалуйста, выберите:', reply_markup=self.button_bot(update))



        application = ApplicationBuilder().token('7507147736:AAEOYdf3erBfJ-x7unESp431YfAgufAAQ50').build()

        start_handler = CommandHandler('start', start)
        application.add_handler(start_handler)

        application.run_polling()

    """async def send_welcome(message: types.Message):
            kb = [
                [
                    KeyboardButton(text="Сможешь повторить это?"),
                    KeyboardButton(text="А это?")
                ],
            ]
            keyboard = ReplyKeyboardMarkup(keyboard=kb)

            await message.reply(
                "Привет!\nЯ Эхобот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.",
                reply_markup=keyboard)

        application.run_polling()"""