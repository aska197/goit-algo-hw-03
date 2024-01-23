from datetime import datetime

def get_days_from_today(date):

    try:
        today = datetime.today()
        date_object = datetime.strptime(date, "%Y-%m-%d")
        delta = today - date_object
        return delta.days
    except ValueError:
        print("Invalid date format. Use 'YYYY-MM-DD' format.")


today_date = datetime.today().strftime("%Y-%m-%d")
days_difference = get_days_from_today("2002-02-19")

print(f"Today is {today_date}, difference in days is: {days_difference}")
