days = int(input())

years = days // 360
days = days % 360

months = days // 30
days = days % 30

print(years, months, days)
