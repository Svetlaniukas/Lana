NAME = "mymodule"


def open_staff_file(file_name, file_delimiter):
    dict_staff = {}
    for_staff_file = open(file_name, 'r')
    for line in for_staff_file:
        if file_name in file_delimiter:
            line.rstrip()
        else:
            (key, val) = line.split(file_delimiter)
            dict_staff[key] = val
            return (key, val), dict_staff
