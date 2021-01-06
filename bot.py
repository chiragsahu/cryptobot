import telebot
import requests
import math

bot = telebot.TeleBot(token='1472008407:AAGHkB_KPARU7DRqiURGdvEDU9mhDuFagi8')
WAZIRX_LIVE_URL = "https://api.wazirx.com/api/v2/depth"

# cryptos = ["/usdtinr",  "btcinr",  "/ltcinr",  "/xrpinr",
#           "/dashinr",  "/ethinr",  "/trxinr",  "/eosinr",
#             "/batinr",  "/wrxinr",  "/maticinr",  "/bchabcinr",
#           "/bnbinr",  "/bttinr",  "/yfiinr",  "/uniinr",  "/linkinr",
#           "/sxpinr",  "/adainr",  "/atominr",  "/xlminr",  "/xeminr",
#             "/zecinr",  "/busdinr",  "/usdtinr"]

cryptos = ["usdtinr",  "btcinr",  "ltcinr",  "xrpinr",  "dashinr",
           "ethinr",  "trxinr",  "eosinr",  "batinr",  "wrxinr",
           "maticinr",  "bchabcinr",  "bnbinr",  "bttinr",  "yfiinr",
           "uniinr",  "linkinr",  "sxpinr",  "adainr",  "atominr",
           "xlminr",  "xeminr",  "zecinr",  "busdinr",  "usdtinr"]


def getApi(crypto):
    response = requests.get(WAZIRX_LIVE_URL, params={'market': crypto})
    data = response.json()
    return data


def formatOutput(rawData):
    data = {}
    output = '''{dash}
      ASK / SELL
{dash}
    PRICE    -  VOL
{dash}{ask}
{dash}

{dash}
      BIDS / BUY
{dash}
    PRICE    -  VOL
{dash}{sell}
'''

    for keys in rawData:
        if rawData[keys]['error'] == 'false':
            output_ask = ""
            output_buy = ""
            for ask in (rawData[keys]['asks'][:5]):
                val = "\n| {:.2f} - {:.4f}|".format(
                    float(ask[0]), float(ask[1]))
                length = math.ceil(len(val)*0.8)
                output_ask += val

            for bid in (rawData[keys]['bids'][:5]):
                output_buy += '\n| {:.2f} - {:.4f} |'.format(
                    float(bid[0]), float(bid[1]))
            data[keys] = output.format(dash = '- '*length,ask=output_ask, sell=output_buy)
        else:
            data[keys] = 'please enter a valid command!'
    return data


def returnPrice(texts):
    results = {}
    for text in texts:
        crypto = text[1:]
        if text.startswith('/') and crypto in cryptos:
            results[crypto] = getApi(crypto)
            results[crypto]['error'] = 'false'
        else:
            results[crypto] = {}
            results[crypto]['error'] = 'true'
        print(results)
    return results


@bot.message_handler(commands=['start'])
def reply(message):
    bot.reply_to(message, 'hello')


@bot.message_handler(func=lambda msg: msg.text is not None and msg.text.startswith('/'))
def tellPrice(message):
    texts = message.text.split()
    rawData = returnPrice(texts)
    finalData = formatOutput(rawData)
    for keys in finalData:
        bot.reply_to(message, finalData[keys])


bot.polling()
