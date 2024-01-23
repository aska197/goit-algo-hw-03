# TASK 1

import random
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



# TASK 2
def get_numbers_ticket(min, max, quantity):

    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= max):
        return []

    unique_numbers_set = set()

    while len(unique_numbers_set) < quantity:
        unique_numbers_set.add(random.randint(min, max))

    result_list = sorted(list(unique_numbers_set))
    return result_list


lottery_numbers = get_numbers_ticket(77, 777, 7)
print("Your lottery numbers:", lottery_numbers)



