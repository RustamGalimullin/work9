from telegram import Bot 
from telegram.ext import Updater, CommandHandler, Filters, Messagehandler 


bot = Bot(token ='5983929855:AAEau7gLvbrzJXkPkhyLFT513mNcNhInrZc')
updater = Updater(token='5983929855:AAEau7gLvbrzJXkPkhyLFT513mNcNhInrZc')
dispatcher = updater.dispatcher

def start(update, context):
    text = update.message.text.split()
    list = []
    for elem in text:
        if 'абв' not in elem:
            list.append(elem)
    context.bot.send_message(update.effective_chat.id, ' '.join(list))


start_handler = Messagehandler(Filters.text, start)
dispatcher.add_handler(start_handler)            

updater.start_polling()
updater.idle()