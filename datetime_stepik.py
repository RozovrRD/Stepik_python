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


#№7
alarm = time(7, 30, 25)

print('Часы:', alarm.strftime('%H'))
print('Минуты:', alarm.strftime('%M'))
print('Секунды:', alarm.strftime('%S'))


#№8
birthday = date(1992, 10, 6)

print('Название месяца:', birthday.strftime('%B'))
print('Название дня недели:', birthday.strftime('%A'))
print('Год:', birthday.strftime('%Y'))
print('Месяц:', birthday.strftime('%m'))
print('День:', birthday.strftime('%d'))


#№9
first_date = min(dates)

iso = 'Дата первого урагана в ISO формате: ' + str(first_date)
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')

print(iso)
print(ru)
print(us)


#№10
andrew = date(1992, 8, 24)

print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number


#№11
first_date = date.fromisoformat(input())
second_date = date.fromisoformat(input())
min_date = min(first_date, second_date)
print(min_date.strftime('%d-%m (%Y)'))


#№12
date_list = list()

n = int(input())
for i in range(n):
    date_list.append(date.fromisoformat(input()))

for dat in sorted(date_list):
    print(dat.strftime('%d/%m/%Y'))


#№13
def print_good_dates(dates):
    answer = list()
    for date in dates:
        if date.year == 1992 and date.month + date.day == 29:
            answer.append(date)
    for item in sorted(answer):
        print(item.strftime('%B %d, %Y'))


#№14
def is_correct(day, month, year):
    try:
        my_date = date(int(year), int(month), int(day))
        return True
    except ValueError:
        return False


#№14
count = 0
while True:
    date_info = input()
    if date_info == 'end':
        break
    date_info = date_info.split('.')
    if is_correct(date_info[0], date_info[1], date_info[2]):
        print("Корректная")
        count += 1
    else:
        print("Некорректная")
print(count)

