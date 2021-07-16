#!/usr/bin/env python3

# Fetch stock market data from alphavantage.co

import requests
import time
import string
import random
import csv


def key_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def api_timing(sleeptime=12.1):
    # free API key allows up to 5 requests per minute,
    # 500 requests per day
    # so we sleep for 12.1 sec to avoid errors (changed to 60s)
    time.sleep(sleeptime)


def get_av_quote(symbol):
    apikey = key_generator()
    apiurl = 'https://www.alphavantage.co/query?'
    apifunction = 'GLOBAL_QUOTE'
    payload = {'function': apifunction, 'symbol': symbol, 'apikey': apikey}
    my_response = requests.get(apiurl, params=payload)
    quote = False
    if (my_response.ok):
        j_data = my_response.json()
        if 'Global Quote' in j_data:
            quote = float(j_data['Global Quote']['05. price'])
    api_timing()
    return quote


def get_av_fx(from_currency, to_currency='EUR'):
    apikey = key_generator()
    apiurl = 'https://www.alphavantage.co/query?'
    apifunction = 'CURRENCY_EXCHANGE_RATE'
    payload = {'function': apifunction,
               'from_currency': from_currency,
               'to_currency': to_currency,
               'apikey': apikey}
    my_response = requests.get(apiurl, params=payload)
    fx_rate = False
    if (my_response.ok):
        j_data = my_response.json()
        if 'Realtime Currency Exchange Rate' in j_data:
            fx_rate = float(
                j_data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    api_timing()
    return fx_rate

i = 1
while(i==1):
    sonic = get_av_quote('SKHCF')
    CD_Projekt = get_av_quote('OTGLF')
    Vulcan_Energy = get_av_quote('VULNF')

    sonic_Price = ['Sonic Healthcare Limited', sonic]
    CD_Projekt_Price = ['CD Projekt Red', CD_Projekt]
    Vulcan_Energy_Price = ['Vulcan Energy Resources', Vulcan_Energy]
    #stockprices = ['Sonic Healthcare Limited,'+str(sonic), 'CD Projekt Red,'+str(CD_Projekt), 'Vulcan Energy Resources,'+str(Vulcan_Energy)]
    stockprices = [sonic_Price, CD_Projekt_Price, Vulcan_Energy_Price]
    hallo = ['a','b','c']
    with open('stockdata.csv', 'w', newline='') as file:
        writer =  csv.writer(file)
        writer.writerows(stockprices)
    print(hallo)
    i=i+1
