from datetime import date

def list_years(dates: list):
    new_dates = []

    for date in dates:
        new_dates.append(date.year)

    return sorted(new_dates)

    







