from controller import parseable_data, solution_equation
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Conversationhandler, Filters
from log import get_id_user, get_input_data, get_result, save_log

bot = Bot(token='5983929855:AAEau7gLvbrzJXkPkhyLFT513mNcNhInrZc')
updater = Updater(token='5983929855:AAEau7gLvbrzJXkPkhyLFT513mNcNhInrZc')
dispatcher = updater.dispatcher

start_calc = 0


def start(update, context):

    context.bot.send_message(update.effective.id, 'я бот калькулятор')
    context.bot.send_message(update.effective.id, 'при решении в примере беру положительные числа')
    context.bot.send_message(update.effective.id, 'я бот калькулятор')
    context.bot.send_message(update.effective.id, 'понимаю знаки * / + -')
    context.bot.send_message(update.effective.id, 'понимаю приоритет действий')
    context.bot.send_message(update.effective.id, 'команда \end отключит меня')
    get_id_user(update.effective_chat.id)
    return start_calc


def receiving_data(update, context):

    data = update.message.text
    get_input_data(data) 
    list_data = parseable_data(data)
    result = solution_equation(list_data)
    get_result(result)
    save_log()
    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')




def cancel(update, context):
    context.bot.send_message(update.effective.id, 'До встречи')
    return Conversationhandler.END



start_handler = CommandHandler('start', start)
receiving_data_handler = MessageHandler(Filters.text & (~Filters.command), receiving_data)    
mes_data_handler = CommandHandler('end', cancel)


conv_handler = Conversationhandler(entry_points=[start_handler], states = {start_calc: [receiving_data_handler]}, fallbacks = [mes_data_handler])

    