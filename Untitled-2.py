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
