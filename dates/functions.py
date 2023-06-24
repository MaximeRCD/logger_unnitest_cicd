from datetime import datetime, timedelta


def today():
    return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")


def substract_days(date_str: str, number_of_days: int):
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    newDate = date - timedelta(days=number_of_days)
    return datetime.strftime(newDate, "%Y-%m-%d %H:%M")
