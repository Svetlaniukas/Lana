import xml
import xml.etree.ElementTree as ET
from json import JSONDecodeError

from flask import json

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
        if len(dict_staff) == 0:
            raise Exception("not able to parse the file")
    return dict_staff


def work_with_db_xml_staff_shift(file_name: xml, key_name: str, val_name: str):
    dict = {}
    tree = ET.parse(file_name)
    root = tree.getroot()
    element = tree.iter()
    for element in root:
        return element.tag, element.attrib

    for child in element:
        if key_name in child.attrib.keys() and val_name in child.attrib.keys():
            key = child.attrib[key_name]
            val = child.attrib[val_name]
            dict[key] = val
            if len(dict) == 0:

except xml.etree.ElementTree.ParseError:
pass

return dict


def work_with_db_json_staff_shift(file_name, root_node_name):
    dict_staff_json = {}
    file_object = open(file_name)
    try:
        dict_staff_json = json.load(file_object)
    except JSONDecodeError as error_code:
        return {}
    if not root_node_name in dict_staff_json.keys():
        return {}
    return dict_staff_json[root_node_name]
