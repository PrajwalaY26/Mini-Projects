from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello, I am Echo Bot! I will repeat everything you say.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    updater = Updater("6564676825:AAGrnd1FH4YXsfUactP7RAvfZ-4J5p05NPg", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
