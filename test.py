def read_staff_from_file():
    d = {}
    for_week_days_shift = open ("staff_week_day.txt", 'r')
    for_staff_weekend_shift = open ("staff_weekend.txt", 'r')
    for line in for_week_days_shift:
        (key, val) = line.split (':')
        d[key] = val
    for line in for_staff_weekend_shift:
        (key, val) = line.split ('=')
        d[key] = val
