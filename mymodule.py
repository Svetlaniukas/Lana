import json
from json import JSONDecodeError
from xml.etree import ElementTree

from _pytest._code import source

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


def work_with_db_xml_staff_shift(file_name, root_node_name):
    dict_staff_xml = {}
    file_object = ElementTree.parse(file_name)
    try:
        dict_staff_xml = file_object
    except SyntaxError as error_code:
        return {}
    return dict_staff_xml[root_node_name]


class XmlDictConfig(dict):

    tree = ElementTree.parse('.xml')
    root = tree.getroot()
    xmldict = XmlDictConfig(root)



   root = ElementTree.XML(xml_string)
   xmldict = XmlDictConfig(root)










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
