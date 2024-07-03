from datetime import datetime

user_date = input('Enter the date in format - YYYY-ММ-DD: ')


def get_days_from_today(date_from_user):
    try:
        date = datetime.strptime(date_from_user, "%Y-%m-%d")
        current_date = datetime.now()
        result = current_date - date
        print(result.days)
    except ValueError:
        print('The entry date isn\'t correct!')


get_days_from_today(user_date)
