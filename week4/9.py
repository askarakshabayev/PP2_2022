from datetime import datetime

now = datetime.now()

print(now)
print(now.day)
print(now.year)
print(now.month)
print(now.strftime('%d.%m.%Y'))

print(now.strftime('%A'))

d = datetime(2018, 3, 15, 20, 45)

print(d.strftime('%d/%m/%Y %H:%M'))