import requests
import json
import time
import datetime


while True:
    requisicao = requests.get('http://api.bitvalor.com/v1/ticker.json')

    informacoes = json.loads(requisicao.text)
    
    print("### COTAÇÃO ###", datetime.datetime.now())
    print('Cotação BitcoinToYou:', informacoes['ticker_24h']['exchanges']['B2U']['last'])
    print('Cotação Foxbit:', informacoes['ticker_24h']['exchanges']['FOX']['last'])
    print('Cotação Mercado Bitcoin:', informacoes['ticker_24h']['exchanges']['MBT']['last'])
    print('Cotação Negocie Coins:', informacoes['ticker_24h']['exchanges']['NEG']['last'])
    print('Cotação FlowBTC:', informacoes['ticker_24h']['exchanges']['FLW']['last'])
    time.sleep(60)

