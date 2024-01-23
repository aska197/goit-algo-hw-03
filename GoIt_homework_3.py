import re
import random
from datetime import datetime


# TASK 1
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



# TASK 3
def normalize_phone(phone_number):

    digits_only = re.sub(r'[^0-9+]', '', phone_number)

    if digits_only.startswith('+380'):
        return digits_only

    elif digits_only.startswith('380'):
        digits_only = '+' + digits_only
        return digits_only

    elif digits_only.startswith('0'):
        digits_only = '+38' + digits_only
        return digits_only


phone_number = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in phone_number]
print("Normalized phone numbers for sending SMS: ", sanitized_numbers)



