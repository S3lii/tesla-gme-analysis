# Import all libraries at the top
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# ========== QUESTION 1 ==========
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print("First 5 rows of Tesla stock data:")
print(tesla_data.head())

# ========== QUESTION 2 ==========
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for table in soup.find_all("table"):
    if table.find("th") and "Tesla Quarterly Revenue" in table.get_text():
        rows = table.find_all("tr")
        for row in rows[1:]:
            cols = row.find_all("td")
            if len(cols) == 2:
                date = cols[0].get_text().strip()
                revenue = cols[1].get_text().strip().replace("$", "").replace(",", "")
                tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])], ignore_index=True)

print("Last 5 rows of Tesla revenue data:")
print(tesla_revenue.tail())

# ========== QUESTION 3 ==========
gamestop = yf.Ticker("GME")
gme_data = gamestop.history(period="max")
gme_data.reset_index(inplace=True)
print("First 5 rows of GameStop stock data:")
print(gme_data.head())

# ========== QUESTION 4 ==========
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for table in soup.find_all("table"):
    if table.find("th") and "GameStop Quarterly Revenue" in table.get_text():
        rows = table.find_all("tr")
        for row in rows[1:]:
            cols = row.find_all("td")
            if len(cols) == 2:
                date = cols[0].get_text().strip()
                revenue = cols[1].get_text().strip().replace("$", "").replace(",", "")
                gme_revenue = pd.concat([gme_revenue, pd.DataFrame([[date, revenue]], columns=["Date", "Revenue"])], ignore_index=True)

print("Last 5 rows of GameStop revenue data:")
print(gme_revenue.tail())

# ========== QUESTION 5 ==========
plt.figure(figsize=(12, 6))
plt.plot(tesla_data['Date'], tesla_data['Close'], color='blue', linewidth=2)
plt.title('Tesla Stock Price Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Close Price (USD)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# ========== QUESTION 6 ==========
plt.figure(figsize=(12, 6))
plt.plot(gme_data['Date'], gme_data['Close'], color='green', linewidth=2)
plt.title('GameStop Stock Price Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Close Price (USD)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()