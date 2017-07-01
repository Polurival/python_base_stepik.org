import datetime

dates = [int(i) for i in input().split()]
days = int(input())

start_date = datetime.date(dates[0], dates[1], dates[2])
plus_days = datetime.timedelta(days=days)
end_date = start_date.__add__(plus_days)

print(end_date.year, end_date.month, end_date.day)

