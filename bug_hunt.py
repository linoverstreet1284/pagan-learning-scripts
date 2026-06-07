import datetime

def calculate_lughnasadh_countdown():
    # BUG 1 & 2 are hidden in these two lines:
    today_date = datetime.date.today()
    lughnasadh = datetime.date(2026, 8, 1)
    
    # Calculate the time difference
    time_remaining = lughnasadh - today_date
    
    # BUG 3 is hidden in this conditional statement:
    if time_remaining == 0:
        print("Blessed Be! Lughnasadh is today!")
    else:
        print(f"There are {time_remaining.days} days left until Lughnasadh.")

calculate_lughnasadh_countdown()
