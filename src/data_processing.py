from typing import List
import yfinance as yf

# Ticker information
START_DATE = '2015-01-01'
END_DATE = '2025-06-01'
TICKERS = ['SPY', 'TLT']

def get_data(tickers: List[str], start: str, end: str):
    """Download and save closed price as CSV files"""
    # Get raw data
    raw_data = yf.download(tickers, start=start, end=end, interval='1d')
    raw_data.to_csv('data/raw.csv')

    # Extract closed price only for stability
    processed_data = raw_data['Close'].dropna()
    processed_data.to_csv('data/price.csv')
    return

if __name__ == "__main__":
    get_data(TICKERS, START_DATE, END_DATE)
