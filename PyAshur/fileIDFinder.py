#Makes bot record file_id of any file sent
import logging
import telegram
from time import sleep
from urllib.error import URLError


def main():
    # Telegram Bot Authorization Token
    bot = telegram.Bot('172323851:AAFTueJhSP2C5MCoQliVIel6Ox11ZFZAMzA')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            update_id = echo(bot, update_id)
        except telegram.TelegramError as e:
            # These are network problems with Telegram.
            if e.message in ("Bad Gateway", "Timed out"):
                sleep(1)
            elif e.message == "Unauthorized":
                # The user has removed or blocked the bot.
                update_id += 1
            else:
                raise e
        except URLError as e:
            # These are network problems on our end.
            sleep(1)


def echo(bot, update_id):

    # Request updates after the last update_id
    for update in bot.getUpdates(offset=update_id, timeout=10):
        # chat_id is required to reply to any message
        chat_id = update.message.chat_id
        update_id = update.update_id + 1
        message = update.message

        if message:
            # Reply to the message
            try:
                bot.sendMessage(chat_id=chat_id,
                            text=message.text)
            except:
                try:
                    bot.sendMessage(chat_id=chat_id,text=message.audio.file_id)
                except:
                    print("do nothing bc I am a really fucking good programmer")

    return update_id


if __name__ == '__main__':
    main()