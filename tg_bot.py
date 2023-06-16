import os
from datetime import datetime

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater
from eth_gas_price import get_gas_price

# from telegram import Bot

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TG')
TELEGRAM_CHAT_ID = os.getenv('CHAT_ID')
URL = "https://cointool.app/gasPrice/eth/"


def new_price(update, context):
    """gas price bot message"""
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['/get_price']], resize_keyboard=True)
    price = get_gas_price(URL)
    current_time = datetime.now()

    context.bot.send_message(
        chat_id=chat.id,
        text=f'The ETH GAS price on time:\
\n{current_time.strftime("%d/%m/%Y %H:%M:%S")}\n\
FAST {price[0]}\n\
NORMAL {price[1]}\n\
SLOW {price[2]}',
        reply_markup=button
    )


def wake_up(update, context):
    """initial greetings"""
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['/start']], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Hello.\n\
This is a bot for getting ETH gas price.\n\
Just press a /get_price button',
        reply_markup=button
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('get_price', new_price))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
