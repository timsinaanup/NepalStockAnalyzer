# NepalStockAnalyzer

A comprehensive tool designed to simplify stock selection in the Nepal Stock Exchange (NEPSE) by leveraging web scraping, data analysis, and machine learning techniques to provide actionable insights for investors.

## Development Status

This project is currently in the development phase. Features and functionalities are being actively improved.

# keywords

- General Data: Normal overview that is looked at superficially.
- Ownership Structure: Breakdown of stock ownership among different holders.
- Fundamentals: Quarterly reports data and key financial indicators.

## API

The tool utilizes the API from ShareHub Nepal to fetch real-time stock market data. Data is extracted using the requests module and processed into a structured format using Pandas.

## Steps:

- Fetch Data: API request is sent to retrieve JSON data.

- Extract Required Information: Necessary fields such as Security Name, Symbol, and Sector are extracted and stored in a Pandas DataFrame.

- Store Data Efficiently: The DataFrame ensures easy access to the stock data for further processing.

## DataFrame Usage

After creating the initial DataFrame, it is imported into another script to process individual stocks separately.

## Key Functionalities

- Fundamental Analysis: Extracts essential stock indicators such as EPS, P/E ratio, and LTP from individual company pages.

- Ownership Breakdown: Scrapes shareholder proportions from the stock details page.

- Data Storage & Processing: Maintains stock data efficiently for machine learning applications.

## Future Enhancements

- Machine Learning Integration: Implement predictive analysis for stock performance.

- Web Interface: Develop a user-friendly UI for visualization and easier access to insights.

- Automated Data Updates: Periodic updates to maintain up-to-date stock information.

Stay tuned for further updates! 🚀

~ Author : Anup Timsina