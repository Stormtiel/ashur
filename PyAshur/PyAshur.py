from telegram import Updater
from telegram.dispatcher import run_async
from time import sleep
import logging
import configparser
from datetime import datetime
import os
import random

#configuration file loading
config = configparser.ConfigParser()
config.read('info.ini')

#Enable debug mode. Prevents anybody other than the owner from sending commands. Reduces error spam.
DEBUG_MODE = False
owner = config.get('Connection','Owner')

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
    name3 = ["Balls", "Thunder", "Fuck", "Butt", "Steak", "Hard", "Rock", "Large", "Huge", "Beef", "Thrust", "Big", "Bigger", "Meat", "Hard", "Fight", "Fizzle", "Run", "Fast", "Drink", "Lots", "Slam", "Chest", "Groin", "Bone", "Meal", "Thorn", "Body", "Squat"]

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
                                + "/song - Sends a random song.\n"
                               # + "/weed - WEEEEEEEEEEEEEEEEEED \n"
                                + "/help - Show list of commands.")

def weed(bot, update):
    bot.sendAudio(update.message.chat_id, "BQADAwAD9QADjNBuCVND9DAbU9S6Ag", "Councilor Vay Hek", "WEED")

def song(bot, update):

    songs = [["BQADAwAD9gADjNBuCaiKvd8et3ktAg","Caravan Palace","Lone Digger"],
             ["BQADAwAD9wADjNBuCdD8ctbcUZJ_Ag","Five Iron Frenzy","It Was A Dark and Stormy Night"]
             ];

    song = songs[random.randint(0, len(songs)-1)]
    file = song[0]
    artist = song[1]
    title = song[2]

    bot.sendAudio(update.message.chat_id, file, artist, title)

def kinkshame(bot, update, args):
    if "@" in ' '.join(args):
        target = ' '.join(args)
    else:
        target = ''

    photos = ["AgADAwADFasxG4zQbgk5ARt59FNJ84v26yoABIurJjLTxGHqqucAAgI",
                "AgADAwADFqsxG4zQbgmeLU8qJeYtkXb36yoABJ5P2Z6ypVtF7ecAAgI",
                "AgADAwADF6sxG4zQbgkxPqwKqBbD9Qn36yoABDDDDdgfM4ml_ucAAgI",
                "AgADAwADGKsxG4zQbgmZ1Pr5uI5tRY4AAewqAAQbv3d31MnNTBTnAAIC",
                "AgADAwADGasxG4zQbgmzG2GWKfY-eTb26yoABMf6FJCQbopE7eMAAgI",
                "AgADAwADG6sxG4zQbglCIbxXXz3jdHIb7yoABB5gGbnLdT65aG8BAAEC",
                "AgADAwADHKsxG4zQbgmeqA6BjVcUOzIW7yoABMILZ36SdBdObXMBAAEC",
                "AgADAwADHasxG4zQbglSLXgtYiKS33UJ7CoABGhUxLefAt84hOcAAgI",
                "AgADAwADGqsxG4zQbgkixkCtpf7iGhD86yoABN-R9pQCplB8BegAAgI",
                "AgADAwADH6sxG4zQbgldDvtQ4XcaOb4V7yoABEQGK46vVoD4AAFuAQABAg",
                "AgADAwADHqsxG4zQbgmn0R7fF6rVIcgb7yoABKYgZowSo9YQNHMBAAEC",
                "AgADAwADIKsxG4zQbgm6ereuhfBw91L26yoABDIbw4kJyPTnmusAAgI",
                "AgADAwADIasxG4zQbgmjeaaVl3bpswf26yoABMzcgtXwX0836OkAAgI",
                "AgADAwADI6sxG4zQbgmTGUrRIO6RUnL3hjEABFjPG65yTBqaL1EAAgI",
                "AgADAwADIqsxG4zQbgkdATXBze1LZdj3hjEABASalwlufLRhYlAAAgI",
                "AgADAwADJKsxG4zQbglAsRpHtyUBZOL46yoABHGm4h0cVdw6NOoAAgI",
                "AgADAwADJqsxG4zQbgl_4BnIZkzQjrIU7yoABGgGJ_XKYIfvTnEBAAEC",
                "AgADAwADJasxG4zQbgkXk-T3pUf_8cMF7CoABHGanjqPA7YwnuYAAgI",
                "AgADAwADJ6sxG4zQbgn6z7CeTwAB6X9tCewqAAT6z_otIrXhJaHlAAIC",
                "AgADAwADKasxG4zQbglysMO1Px4102_66yoABFZlB8F8Lv9xmOcAAgI",
                "AgADAwADKKsxG4zQbgmXh_-vmMOdbpv46yoABGXvmrLUh9kwO-cAAgI",
                "AgADAwADKqsxG4zQbgl76v4rYmg7HhAU7yoABBfExK9jDpyQC3MBAAEC",
                "AgADAwADK6sxG4zQbglqKL6v4G8pCr3_6yoABGDAIalQlwXNU-sAAgI",
                "AgADAwADLKsxG4zQbgnOO6p91tk5kF4J7CoABL9MPp34InF6NugAAgI",
                "AgADAwADLasxG4zQbgkjTfZpRsM4t8f1hjEABEF0nwvn6xgTU1EAAgI",
                "AgADAwADLqsxG4zQbgnOdSDekS4PYSUH7CoABB9-YtOON9LIE-wAAgI",
                "AgADAwADL6sxG4zQbgnVqVLXJVBHwN8H7CoABDinX41Md3R8_-YAAgI",
                "AgADAwADMKsxG4zQbgkvn4Je5DgAAb29-usqAATUdnN4VuYeCRLnAAIC",
                "AgADAwADMasxG4zQbgntrjpsKkEim24c7yoABKyrQS-bUkvURHEBAAEC",
                "AgADAwADMqsxG4zQbgl8l5u60GsAAcMbGu8qAAQ7WHs8yI7JutpxAQABAg",
                "AgADAwADM6sxG4zQbgk_Ja9qN9ZrMM0X7yoABF2MUFrEECyH5HMBAAEC",
                "AgADAwADNKsxG4zQbgnZoiSGA9Tbe9YG7CoABEHYVLtY11mAoesAAgI",
                "AgADAwADNasxG4zQbglbSCiL9eVMMboZ7yoABODPeyhYyaHUtW0BAAEC"]

    bot.sendPhoto(update.message.chat_id, photos[random.randint(0, len(photos)-1)], target)

#logs icnoming messages
def any_message(bot, update):
    if(DEBUG_MODE == True):
        if(update.message.from_user.username != owner):
            bot.sendMessage(update.message.chat_id, "I'm sorry, debug mode is enabled and I can only receive commands from my owner at the moment.")
            #there's probably a way to make this less wordy, but it's okay for now
            raise ValueError('Unauthorized user attempted command.')

    else:
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
    #pass the token
    token = config.get("Connection","Token")
    group = config.get("Connection","Group")

    updater = Updater(token, workers=10)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # add important handlers
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)
    dp.addUnknownTelegramCommandHandler(unknown_command)

    dp.addTelegramRegexHandler('.*', any_message)

    #non-essential handlers
    dp.addTelegramCommandHandler('hiashur', hiashur)
    dp.addTelegramCommandHandler('norn', norn)
    dp.addTelegramCommandHandler('weed', weed)
    dp.addTelegramCommandHandler('song', song)
    dp.addTelegramCommandHandler('kinkshame', kinkshame)

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