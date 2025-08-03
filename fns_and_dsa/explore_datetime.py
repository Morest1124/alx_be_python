from datetime import datetime, timedelta

def get_current_datetime():
    return datetime.now()

def display_current_datetime():
    current_date = get_current_datetime()
    print(current_date.strftime("%d-%m-%Y %H:%M:%S"))

def calculate_future_date():
    current_date = get_current_datetime()
    number_of_days = int(input('Enter how many days you want to add: '))
    future_date = current_date + timedelta(days=number_of_days)
    print(future_date.strftime("%Y-%m-%d"))

display_current_datetime()
calculate_future_date()
