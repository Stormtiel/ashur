from telegram import Updater
from telegram.dispatcher import run_async
from time import sleep
import logging
import configparser
from datetime import datetime
import os
import random

# Enable Logging
logging.basicConfig(level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',\
        filemode='w',
        filename= os.getcwd() + '/logs/' + datetime.strftime(datetime.now(), '%Y-%m-%d %H-%M-%S') + '.log'
        )
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

logger = logging.getLogger(__name__)

last_chat_id = 0


# Command handlers
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hello, ' + update.message.from_user.first_name + '.')

def hiashur(bot,update):
    bot.sendMessage(update.message.chat_id, text='Hello, ' + update.message.from_user.first_name + '.')

def norn(bot,update):
    name1 = ["Crunch", "Olaf", "Beef", "Chunk", "Smoke", "Brick", "Crash", "Thick", "Bold", "Buff", "Drunk", "Punch", "Crud", "Grizzle", "Slab", "Hack", "Big"]
    name2 = ["Mac", "Mc", ""]
    name3 = ["Thunder", "Fuck", "Butt", "Steak", "Hard", "Rock", "Large", "Huge", "Beef", "Thrust", "Big", "Bigger", "Meat", "Hard", "Fight", "Fizzle", "Run", "Fast", "Drink", "Lots", "Slam", "Chest", "Groin", "Bone", "Meal", "Thorn", "Body", "Squat"]

    n1 = name1[random.randint(0, len(name1)-1)]
    n2 = name2[random.randint(0, len(name2)-1)]
    n3 = name3[random.randint(0, len(name3)-1)]
    n4 = name3[random.randint(0, len(name3)-1)].lower()

    bot.sendMessage(update.message.chat_id, text= n1 + " " + n2 + n3 + n4)

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text= "Greetings, I am Cephalon Ashur. I specialize in reminding Operators of alerts that pop up on the Warframe RSS feed. I can also obey a select number of commands: \n \n" +
                                "/hiashur - Say hello.\n"
                               # + "/watch - Give me a keyword to watch for.\n"
                               # + "/watching - Get a list of all keywords I'm watching.\n"
                               # + "/showall - Toggles showing alerts based on keywords.\n"
                               # + "/blabber - Toggles me blabbering alerts at you.\n"
                               # + "/npc - I'll send you a random Warframe NPC voice clip.\n"
                                + "/norn - Generates a Norn name.\n"
                               # + "/weed - WEEEEEEEEEEEEEEEEEED \n"
                                + "/help - Show list of commands.")

#logs icnoming messages
def any_message(bot, update):
    # Save last chat_id to use in reply handler
    global last_chat_id
    last_chat_id = update.message.chat_id

    logger.info("%d > %s - %s %s: %s" %
                (update.message.chat_id,
                 update.message.from_user.username,
                 update.message.from_user.first_name,
                 update.message.from_user.last_name,
                 update.message.text))


#error message when unknown command
def unknown_command(bot, update):
    bot.sendMessage(update.message.chat_id, text='I\'m sorry, I don\'t know what you just said. Try /help.')


#example async handler
@run_async
def message(bot, update, **kwargs):

    sleep(2)  # IO-heavy operation here
    bot.sendMessage(update.message.chat_id, text='Echo: %s' %
                                                 update.message.text)


# CLI handlers
def cli_reply(bot, update, args):
    if last_chat_id is not 0:
        bot.sendMessage(chat_id=last_chat_id, text=' '.join(args))


def cli_noncommand(bot, update, update_queue):
    update_queue.put('/%s' % update)


def unknown_cli_command(bot, update):
    logger.warn("Command not found: %s" % update)


def error(bot, update, error):
    """ Print error to console """
    logger.warn('Update %s caused error %s' % (update, error))


def main():
    #configuration file loading
    config = configparser.ConfigParser()
    config.read('info.ini')

    # Create the EventHandler and pass it your bot's token.
    token = config.get("Connection","Token")
    group = config.get("Connection","Group")

    updater = Updater(token, workers=10)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # add important handlers
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)
    dp.addUnknownTelegramCommandHandler(unknown_command)

    dp.addTelegramMessageHandler(message)
    dp.addTelegramRegexHandler('.*', any_message)

    #non-essential handlers
    dp.addTelegramCommandHandler('hiashur', hiashur)
    dp.addTelegramCommandHandler('norn', norn)

    #CLI handlers
    dp.addStringCommandHandler('reply', cli_reply)
    dp.addUnknownStringCommandHandler(unknown_cli_command)
    dp.addStringRegexHandler('[^/].*', cli_noncommand)

    #Error handler
    dp.addErrorHandler(error)

    #start bot and start polling
    update_queue = updater.start_polling(poll_interval=0.1, timeout=10)

    # Start CLI-Loop
    while True:
        try:
            text = raw_input()
        except NameError:
            text = input()

        # Gracefully stop the event handler
        if text == 'stop':
            updater.stop()
            break

        # else, put the text into the update queue to be handled by our handlers
        elif len(text) > 0:
            update_queue.put(text)

if __name__ == '__main__':
    main()