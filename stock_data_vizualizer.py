# A program that uses stock data to produce graphs and charts based on user constraints

import matplotlib.pyplot as plt
from datetime import datetime
import requests

def main():
    run_program = True
    while run_program == True:
       
       #stock symbols
       symbols = get_stock_symbol()
       if symbols:
        print("Stock Symbols: ")
        for symbol in symbols:
            print(symbol)
       
        # ^where program should go
        answer = input("Would you like to view more stock data? (y/n)")
        if answer == "n":
            run_program = False
        else:
            continue
        
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
                symbols = [item['symbol'] for item in data['data']]
                return symbols
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    return symbol

#def get_chart_type():
    #return chart
    
#def get_time_series():
    #return timeSeries
    
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
    
## YYYY-MM-DD
main()