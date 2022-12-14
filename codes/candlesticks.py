from datetime import date
from nsepy import get_history
import pandas as pd

def ticker_data(ticker, start, end):

	stock = get_history(symbol=ticker, start=start, end=end)

	df = stock.copy()
	df = df.reset_index()
	df = df.drop(['Series', 'Prev Close', 'Last', 'Turnover', '%Deliverble', 'Trades'], axis=1)
	df = df.rename({'Open': 'open_price', 'Close': 'close_price', 'High':'high', 'Low' : 'low', 'Volume' : 'volume'}, axis='columns')
	df.index = df.Date
	return df


print(ticker_data('INFY', date(2018,1,1), date(2020,9,1)))
