from simple_bot import run_simple_bot
from currency_bot import run_currency_bot

if __name__ == '__main__':
    # константа с вашим токеном, полученным из BotFather
    TOKEN = "6011813145:AAF5avWYedNHKaozW7Pxe6LkshbtY48ityU"
    # YOUR_TOKEN"

    # запустить простого демо-бота
    # run_simple_bot(TOKEN)

    # # запустить бота курсов валют
    run_currency_bot(TOKEN)