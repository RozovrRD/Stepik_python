#TODO: realize all stepik datetime tasks

from datetime import date, time

#№1
print(date.today())


#№2
hurricane_andrew = date(1992, 8, 24)
print(hurricane_andrew.weekday())


#№3
dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11),
         date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21),
         date(1666, 6, 6), date(1968, 5, 26)]

for date in dates:
    print(date.year, '-', 'Q', (date.month + 2) // 3, sep='')


#№4
def get_min_max(dates):
    if len(dates) == 0:
        return tuple()
    return min(dates), max(dates)


#№5
def get_date_range(date1, date2):
    if date1 > date2:
        return list()
    first_num = date1.toordinal()
    last_num = date2.toordinal()
    return [date.fromordinal(day) for day in range(first_num, last_num+1)]


#№6
def saturdays_between_two_dates(date1, date2):
    start = min(date1.toordinal(), date2.toordinal())
    end = max(date1.toordinal(), date2.toordinal())
    count_days = 0
    for day in range(start, end+1):
        if date.fromordinal(day).weekday() == 5:
            count_days += 1
    return count_days