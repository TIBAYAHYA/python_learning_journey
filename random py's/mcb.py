import yfinance as yf
import pandas as pd
import numpy as np
import talib

# Step 1: Download S&P 500 Stocks Data
tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].tolist()
data = yf.download(tickers, start="2020-01-01", end="2023-01-01")

# Step 2: Create Buy Signal Rules
def buy_signal(df):
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['SMA_200'] = talib.SMA(df['Close'], timeperiod=200)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    df['Buy_Signal'] = np.where((df['SMA_50'] > df['SMA_200']) & (df['RSI'] < 30), True, False)
    return df

data = data.groupby('Ticker').apply(buy_signal)

# Step 3: Backtest the Rules
# This is a simplified example. For a full backtest, consider using a library like backtrader.
data['Future_Close'] = data.groupby('Ticker')['Close'].shift(-5)
data['Price_Change'] = (data['Future_Close'] - data['Close']) / data['Close']
data['Buy_Signal'] = np.where(data['Price_Change'] >= 0.025, True, False)

# Step 4: Output to Excel
data.to_excel('buy_signals.xlsx', sheet_name='Buy Signals')

print("Script executed successfully and data saved to buy_signals.xlsx")