NAME = "mymodule"


def open_staff_file(file_name, file_delimiter):
    dict_staff = {}
    for_staff_file = open(file_name, 'r')
    for line in for_staff_file:
        if file_delimiter in line:
            (key, val) = line.split(file_delimiter)
            key.strip()
            val.strip('\n')
            key.strip()
            val.strip('\n')

            dict_staff[key] = val
    return dict_staff
