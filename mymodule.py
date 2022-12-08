NAME = "mymodule"


def read_staff_from_file(file_name, file_delemiter):
    dict_staff = {}
    for_week_days_shift = open(file_name, 'r')
    for line in for_week_days_shift:
        (key, val) = line.split(file_delemiter)
        dict_staff[key] = val
        print()
    return dict_staff


