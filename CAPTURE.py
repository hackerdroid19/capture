import os
from telegram.ext import Updater, MessageHandler, Filters


def process_message(update, context):

    text = update.message.text

    if str(text).__contains__('#channel'):
        context.bot.send_message(
            chat_id='YOUR_CHANNEL_ID',
            text=str(text).replace('#channel', '')
        )


if __name__ == '__main__':

    updater = Updater(token=os.environ['TOKEN'], use_context=True)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))
    updater.start_polling()

    print('Bot is polling')

    updater.idle()
    updater = Updater("1909365203:AAG8KtuhUcZp_QUEOovitQ-q5fdL13OAPh8", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("sumar", sumar))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, pizza))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()