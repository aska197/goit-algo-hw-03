from datetime import datetime, timedelta
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



# TASK 4

# import random
# from faker import Faker

# users = [
#     {'name': 'John Doe', 'birthday': '1985.01.23'},
#     {'name': 'Jane Smith', 'birthday': '1990.01.27'},
#     {'name': 'Anthony Shaw', 'birthday': '1978.08.12'},
#     {'name': 'Kelly Fisher', 'birthday': '1973.05.21'},
#     {'name': 'Jennifer Soto', 'birthday': '1972.11.17'},
#     {'name': 'Steven West', 'birthday': '1979.04.05'},
#     {'name': 'Zachary Walker', 'birthday': '1973.09.03'},
#     {'name': 'Elizabeth Reynolds', 'birthday': '1991.11.22'},
#     {'name': 'Dillon Frank', 'birthday': '1966.01.28'},
#     {'name': 'Kristen Goodman', 'birthday': '1965.02.25'},
#     {'name': 'Robert Alvarez', 'birthday': '1980.04.01'},
#     {'name': 'Matthew Hill', 'birthday': '1965.10.23'},
#     {'name': 'Joseph Lee', 'birthday': '1982.01.07'},
#     {'name': 'Caleb Espinoza', 'birthday': '1963.08.29'},
#     {'name': 'Laura Lopez', 'birthday': '1994.05.10'},
#     {'name': 'Michael Davis', 'birthday': '1967.04.02'},
#     {'name': 'Anthony Dawson', 'birthday': '1997.09.12'},
# ]

# fake = Faker()

# # Generate 5 additional random names and dates
# additional_users = [
#     {"name": fake.name(), "birthday": fake.date_of_birth(
#         minimum_age=18, maximum_age=65).strftime("%Y.%m.%d")}
#     for _ in range(5)
# ]

# # Extend the original users list with the additional users
# users.extend(additional_users)

# # Print the updated users list
# for user in users:
#     print(user)


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year+1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:

            if birthday_this_year.weekday() in [5, 6]:
                monday_after_birthday = birthday_this_year + \
                    timedelta(days=(7 - birthday_this_year.weekday()))
                congradulation_date = monday_after_birthday.strftime(
                    "%Y.%m.%d")
            else:
                congradulation_date = birthday_this_year.strftime("%Y.%m.%d")

            upcoming_birthdays.append(
                {"name": user["name"], "congradulation_date": congradulation_date})

    return upcoming_birthdays


users = [
    {'name': 'John Doe', 'birthday': '1985.01.23'},
    {'name': 'Jane Smith', 'birthday': '1990.01.27'},
    {'name': 'Anthony Shaw', 'birthday': '1978.08.12'},
    {'name': 'Kelly Fisher', 'birthday': '1973.05.21'},
    {'name': 'Jennifer Soto', 'birthday': '1972.11.17'},
    {'name': 'Steven West', 'birthday': '1979.04.05'},
    {'name': 'Zachary Walker', 'birthday': '1973.09.03'},
    {'name': 'Elizabeth Reynolds', 'birthday': '1991.11.22'},
    {'name': 'Dillon Frank', 'birthday': '1966.01.28'},
    {'name': 'Kristen Goodman', 'birthday': '1965.02.25'},
    {'name': 'Robert Alvarez', 'birthday': '1980.04.01'},
    {'name': 'Matthew Hill', 'birthday': '1965.10.23'},
    {'name': 'Joseph Lee', 'birthday': '1982.01.07'},
    {'name': 'Caleb Espinoza', 'birthday': '1963.08.29'},
    {'name': 'Laura Lopez', 'birthday': '1994.05.10'},
    {'name': 'Michael Davis', 'birthday': '1967.04.02'},
    {'name': 'Anthony Dawson', 'birthday': '1997.09.12'},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("This week's list of birthdays' congradulations:", upcoming_birthdays)
