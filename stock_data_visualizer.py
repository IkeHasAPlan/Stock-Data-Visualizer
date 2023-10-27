# A program that uses stock data to produce graphs and charts based on user constraints
# Basis of code made by Issac.

import matplotlib.pyplot as plt
from datetime import datetime
import requests
import json
#from alpha_vantage.timeseries import TimeSeries

def main():
    run_program = True
    while run_program:
        key = "IZ2BMG7IZUT81I82"
        start_date, end_date = get_date()
        time_series = get_time_series()
        symbols = get_stock_symbol()
        data = retrieve_data(time_series, symbols, key)

        answer = input("Would you like to view more stock data? (y/n)")
        if answer == "n":
            run_program = False

def get_stock_symbol():
    while True:
        api_key = "IZ2BMG7IZUT81I82"
        url = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={api_key}"

        try:
            response = requests.get(url)
            data = response.json()
            if "Error Message" in data:
                print("Error: Unable to retrieve stock symbol.")
                return None
            else:
                symbols = [item['symbol'] for item in data['symbols']]
                return symbols
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
        #what am I missing to get this part working?

def retrieve_data(function: str, symbol: str, api_key: str ):
    url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)

    return parsed

def get_time_series():
    while True:
        try: 
            print("Select the Time Series of the chart you want to Generate")
            print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
            time_series_choice = int(input("Enter the time series option (1, 2, 3, 4): "))

            if time_series_choice == 1:
                return "TIME_SERIES_INTRADAY"
            elif time_series_choice == 2:
                return "TIME_SERIES_DAILY"
            elif time_series_choice == 3:
                return "TIME_SERIES_WEEKLY"
            elif time_series_choice == 4:
                return "TIME_SERIES_MONTHLY"
            else:
                print("Invalid option. Please select 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_date():
    while True:
        start_d = input("Enter the start date (YYYY-MM-DD): ")
        end_d = input("Enter the end date (YYYY-MM-DD): ")

        try:
            start_date = datetime.strptime(start_d, "%Y-%m-%d")
            end_date = datetime.strptime(end_d, "%Y-%m-%d")

            if start_date <= end_date:
                return start_date, end_date
            else:
                print("Start date must be before or equal to the end date.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

main()