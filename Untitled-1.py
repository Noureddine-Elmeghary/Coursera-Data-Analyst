import yfinance as yf

# Download Tesla stock data
tesla_data = yf.download('TSLA')

# Reset the index to move Date from index to a column
tesla_data.reset_index(inplace=True)

# Display the first 5 rows
print(tesla_data.head())
