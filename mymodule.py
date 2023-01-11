"""
    module is open different types of files and return dictionary
"""
import xml
import xml.etree.ElementTree as ET
from json import JSONDecodeError
import json
import sqlite3

NAME = "mymodule"

"""
    function is open files an return dictionary
"""


def open_staff_file(file_name, file_delimiter):
    dict_staff = {}
    try:
        for_staff_file = open(file_name, "r", encoding="utf-8")
        for line in for_staff_file:
            if file_delimiter in line:
                (key, val) = line.split(file_delimiter)
                key.strip()
                val.strip('\n')
                key.strip()
                val.strip('\n')
                dict_staff[key] = val
    except FileNotFoundError:
        print("FileExistsError")
    return dict_staff


"""
    function is open xml_files and return dictionary
"""


def work_with_db_xml_staff_shift(file_name, key_name, val_name):
    xml_dict = {}
    try:
        tree = ET.parse(file_name)
        element = tree.iter()

        for child in element:
            keys = child.attrib.keys()
            if key_name in keys and val_name in keys:
                key = child.attrib[key_name]
                val = child.attrib[val_name]
                xml_dict[key] = val
    except xml.etree.ElementTree.ParseError:
        print("FileExistsError")
    return xml_dict


"""
    function is open json_files and return dictionary
"""


def work_with_db_json_staff_shift(file_name, root_node_name):
    json_dict = {}
    file_object = open(file_name, encoding="utf-8")
    try:
        json_dict = json.load(file_object)
    except JSONDecodeError:
        return {}
    if root_node_name not in json_dict.keys():
        return {}
    return json_dict[root_node_name]


"""Returns data from an SQL query as a list of dicts."""


def work_with_sql_lite_db_files(file_name, key_name, val_name, time_table):
    db_dict = {}
    try:
        with sqlite3.connect(file_name) as mydict:
            cursor = mydict.cursor()
            query = "SELECT {},{} FROM {}".format(key_name, val_name, time_table)
            cursor.execute(query)
            mydict = cursor.fetchall()
            for row in mydict:
                (key, value) = row
                db_dict[key] = value
    except (sqlite3.Error, sqlite3.OperationalError) as e:
        print(f"The Error '{e}' accurred")
    return db_dict
