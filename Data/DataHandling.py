import yfinance as yf
import datetime

print('yfinance version = ' + yf.__version__)

#TODO: 
#need to know how to open window in desktop mode
#Make an actual UI window

def giveData(stockSymbol):

    tickerdata = yf.Ticker(stockSymbol)
    tickerinfo = tickerdata.info
    investment = tickerinfo['shortName']

    today = datetime.datetime.today().isoformat()

    tickerDF = tickerdata.history(period = '1mo')
    #priceYest = tickerDF['Close'].iloc[-2]
    #print(investment + ' price last = ' + str(pricelast))
    
    return tickerDF,investment,today

def firstPage():
    print('Welcome to Matts stock App')
    
    tsla = 'tsla'
    qcom = 'qcom'
    amd = 'amd'

#Use Python3 for command prompt
#iloc used to get range of data 
def main():

    symbol = input("Enter Symbol: ")
    data, investment, today = giveData(symbol)

    print('Investment: ' + investment)

    print('Today = ' + today)

    pricelast = data['Close']

    #print(data)
    print(pricelast)

if __name__ == '__main__':
    main()