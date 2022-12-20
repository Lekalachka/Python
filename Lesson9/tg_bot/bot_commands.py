from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

from spy import *

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    help_msg = '/hi - приветствие\n/time - показать текущее время\n' \
               '/help - отобразить эту справку\n' \
               '/sum 5 2 - получение суммы чисел 5 и 2'
    update.message.reply_text('/hi\n/time\n/help\n/sum 1 2\n/dif 9 8')

#  /time
def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

# /sum 12 25
def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/sum', '12+3j', '25'
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')


# /csum 12 25
def csum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/sum', '12+3j', '25'
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')


def dif_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/dif', '12+3j', '25'
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')


def cdif_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # '/cdif', '12+3j', '25'
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')