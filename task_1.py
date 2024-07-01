from datetime import datetime

user_date = input('Enter the date in format - YYYY-ММ-DD: ')
date = datetime.strptime(user_date, "%Y-%m-%d")


def get_days_from_today(date_from_user):
    current_date = datetime.now()
    result = current_date - date_from_user
    print(result.days)


get_days_from_today(date)
