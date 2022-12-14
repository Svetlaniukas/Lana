import json

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


def work_with_db_json_staff_shift(file_name, root_node_name):
    dict_staff_json = {}
    file_object = open(file_name)
    dict_staff_json = json.load(file_object)
    return dict_staff_json[root_node_name]
