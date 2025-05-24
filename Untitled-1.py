import yfinance as yf

# Download Tesla stock data
tesla_data = yf.download('TSLA')

# Reset the index to move Date from index to a column
tesla_data.reset_index(inplace=True)

# Display the first 5 rows
print(tesla_data.head())
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for Tesla revenue data
url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'

# Fetch the page
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')

# Initialize the revenue table variable
tesla_revenue_table = None

# Find the table that contains "Tesla Quarterly Revenue"
for table in soup.find_all('table'):
    if "Tesla Quarterly Revenue" in table.text:
        tesla_revenue_table = table
        break

# Check if the table was found
if tesla_revenue_table is None:
    raise Exception("Tesla revenue table not found on the page.")

# Parse the table and extract the data
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in tesla_revenue_table.tbody.find_all("tr"):
    cols = row.find_all("td")
    if cols:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        if revenue:  # Ensure revenue is not empty
            tesla_revenue = pd.concat(
                [tesla_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])],
                ignore_index=True
            )

# Display the last five rows
print(tesla_revenue.tail())

#q1
import yfinance as yf

# Download GameStop stock data
gme_data = yf.download('GME')

# Reset the index to move 'Date' into a column
gme_data.reset_index(inplace=True)

# Display the first five rows
print(gme_data.head())

#q2
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for GameStop revenue data
url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'

# Fetch HTML content
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')

# Find the table containing "GameStop Quarterly Revenue"
gme_revenue_table = None
for table in soup.find_all('table'):
    if "GameStop Quarterly Revenue" in table.text:
        gme_revenue_table = table
        break

# Raise error if table is not found
if gme_revenue_table is None:
    raise Exception("GameStop revenue table not found on the page.")

# Extract data into DataFrame
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in gme_revenue_table.tbody.find_all("tr"):
    cols = row.find_all("td")
    if cols:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace("$", "").replace(",", "")
        if revenue:
            gme_revenue = pd.concat(
                [gme_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])],
                ignore_index=True
            )

# Display the last five rows
print(gme_revenue.tail())

#q6
import matplotlib.pyplot as plt

def make_graph(data, stock, title):
    plt.figure(figsize=(10,6))
    plt.plot(data['Date'], data['Close'], label=f"{stock} Closing Price")
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()
make_graph(gme_data, 'GME', 'GameStop Stock Price Over Time')
