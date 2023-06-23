import datetime as dt 

def getTodayString():
    """
    Return a string representation of the current date in the format "YYYY-MM-DD".

    Args:
        tz (None): Optional timezone parameter (not used in the function).

    Returns:
        str: A string representing the current date in the format "YYYY-MM-DD".
    """
    now = dt.datetime.now()
    todayString = dt.datetime.strftime(now, "%Y-%m-%d %H:%M")
    return todayString

