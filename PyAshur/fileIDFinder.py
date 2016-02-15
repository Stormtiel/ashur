#super janky bot that responds to sent files with the file id

from telegram import Updater
from telegram.dispatcher import run_async

fileids = open('fileids.txt','a')

def any_message(bot, update):
    global last_chat_id
    last_chat_id = update.message.chat_id

    logger.info("New message\nFrom: %s\nchat_id: %d\nText: %s" %
                (update.message.from_user,
                 update.message.chat_id,
                 update.message.text))


def unknown_command(bot, update):
    bot.sendMessage(update.message.chat_id, text='Command not recognized!')


@run_async
def message(bot, update, **kwargs):

    #TODO: make this more flexible and not error when not sent a photo
    sleep(2)
    fileid = update.message.photo[0].file_id
    bot.sendMessage(update.message.chat_id, fileid)
    fileids.write("\"" + fileid + "\",\n")


def cli_reply(bot, update, args):
    if last_chat_id is not 0:
        bot.sendMessage(chat_id=last_chat_id, text=' '.join(args))


def cli_noncommand(bot, update, update_queue):
    update_queue.put('/%s' % update)


def unknown_cli_command(bot, update):
    logger.warn("Command not found: %s" % update)


def error(bot, update, error):
    logger.warn('Update %s caused error %s' % (update, error))


def main():
    config = configparser.ConfigParser()
    config.read('info.ini')

    token = config.get("Connection","Token")
    updater = Updater(token, workers=10)

    dp = updater.dispatcher

    dp.addUnknownTelegramCommandHandler(unknown_command)
    dp.addTelegramMessageHandler(message)
    dp.addTelegramRegexHandler('.*', any_message)

    dp.addStringCommandHandler('reply', cli_reply)
    dp.addUnknownStringCommandHandler(unknown_cli_command)
    dp.addStringRegexHandler('[^/].*', cli_noncommand)

    dp.addErrorHandler(error)

    update_queue = updater.start_polling(poll_interval=0.1, timeout=10)

    # Start CLI-Loop
    while True:
        try:
            text = raw_input()
        except NameError:
            text = input()

        if text == 'stop':
            fileids.close()
            updater.stop()
            break

        elif len(text) > 0:
            update_queue.put(text)

if __name__ == '__main__':
    main()