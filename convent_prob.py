import convert_utils
a = input('Введите программу: ')
b = int(input('Введите число: '))
c = 0
if a == 'temperature':
    c = convert_utils.temperature(b)
elif a == 'hours_seconds':
    c = convert_utils.hours_seconds(b)
elif a == 'hours_minutes':
    c = convert_utils.hours_minutes(b)
elif a == 'hours_days':
    c = convert_utils.hours_days(b)
elif a == 'days_hours':
    c = convert_utils.days_hours(b)
elif a == 'days_minutes':
    c = convert_utils.days_minutes(b)
print(c)