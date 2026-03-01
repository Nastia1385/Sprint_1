# Задание 1
time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_values = time_string.replace(',', ' ').split()
total_minutes = 0

for time in time_values:
    if 'h' in time:
        hours_num = int(time.replace('h', ''))
        total_minutes += hours_num * 60
    elif 'm' in time:
        minutes_num = int(time.replace('m', ''))
        total_minutes += minutes_num
    elif 's' in time:
        seconds_num = int(time.replace('s', ''))
        if seconds_num % 60 == 0:
            total_minutes += seconds_num // 60

print(f'Общее количество минут: {total_minutes}')
