from simple_bot import run_simple_bot
from currency_bot import run_currency_bot

if __name__ == '__main__':
    # константа с вашим токеном, полученным из BotFather
    TOKEN = "YOUR_TOKEN"

    # запустить простого демо-бота
    # run_simple_bot(TOKEN)

    # # запустить бота курсов валют
    run_currency_bot(TOKEN)
