import json
import logging
import urllib.request

from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler


def get_check_ins():
    """Fetch the current and maximum occupation of Jumpers Darmstadt as JSON and decode the result."""
    with urllib.request.urlopen(
            "https://www.jumpers-fitness.com/club-checkin-number/7/Jumpers.JumpersFitnessTld") as url:
        data = json.load(url)

        max_check_ins = data["maxCheckinsAllowed"]
        checked_in = data["countCheckedInCustomer"]

        return checked_in, max_check_ins


# Command handlers
def start_command(update: Update, context: CallbackContext):
    """Send a welcome message when the command /start is issued."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello! To get the current occupation of Jumpers Darmstadt, type /occupation."
    )


def occupation_command(update: Update, context: CallbackContext):
    """Send a message containing the current occupation."""
    checked_in, max_check_ins = get_check_ins()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Checked in: " + str(checked_in) + "\nMaximum: " + str(max_check_ins)
    )


def help_command(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Type /occupation to get the current occupation of Jumpers Darmstadt."
    )


def main():
    """Initialize the bot."""
    # Pass your token to the Updater.
    updater = Updater(token='TOKEN')
    dispatcher = updater.dispatcher

    # Define command handlers for the available commands
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('occupation', occupation_command))
    dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    main()
