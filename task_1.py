from datetime import datetime

user_date = input('Enter the date in format - YYYY-ММ-DD: ')


def get_days_from_today(date_from_user):
    try:
        date = datetime.strptime(date_from_user, "%Y-%m-%d")
        current_date = datetime.now()
        result = current_date - date
        return result.days
    except ValueError:
        print('The entry date isn\'t correct!')


print(f'Кількість днів від {user_date} = {get_days_from_today(user_date)}')
