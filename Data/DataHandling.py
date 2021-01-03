import yfinance as yf
import datetime

print('yfinance version = ' + yf.__version__)


def giveData(stockSymbol):

    tickerdata = yf.Ticker(stockSymbol)
    tickerinfo = tickerdata.info
    investment = tickerinfo['shortName']
    print('Investment: ' + investment)

    today = datetime.datetime.today().isoformat()
    print('Today = ' + today)

    tickerDF = tickerdata.history(period = '1m', start= '2020-12-1', end=today[:10])
    #pricelast = tickerDF['Close'].iloc[-1]
    #priceYest = tickerDF['Close'].iloc[-2]
    #print(investment + ' price last = ' + str(pricelast))

    #print(tickerDF)
    return tickerDF


def main():

    symbol = input("Enter Symbol: ")

    data = giveData(symbol)
    print(data)

if __name__ == '__main__':
    main()