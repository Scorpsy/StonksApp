import yfinance as yf
import datetime

print('yfinance version = ' + yf.__version__)

def yfinancetut(tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    investment = tickerinfo['shortName']
    print('Investment: ' + investment)

    today = datetime.datetime.today().isoformat()
    print('Today = ' + today)

yfinancetut('TSLA')