# A program that uses stock data to produce graphs and charts based on user constraints

import matplotlib.pyplot as plt
from datetime import datetime

def main():
    run_program = True
    while run_program == True:
        print("Hello World")

        symbol = input("Enter the stock symbol for the company: ")
        chart_type = input("Enter the chart type you would like: ")
        time_series_function = input("Enter the time series function you want to use: ")
        start_date = input("Enter the beginning date in YYYY-MM-DD format: ")
        end_date = input("Enter the end date in YYYY-MM-DD format: ")
        # ^where program should go
        answer = input("Would you like to view more stock data? (y/n)")
        if answer == "n":
            run_program = False
        else:
            continue
        
#def get_stock_symbol():
    #return symbol

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