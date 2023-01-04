"""
    module is open different types of files and return dictionary
"""
from sqlite3 import Error
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


"""
    function is open sql_lite_db_files and return dictionary
"""


def run_query(self, query, parameters=()):
    with sqlite3.connect(self.db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    try:
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
        select_posts = "SELECT * FROM posts"
        posts = execute_read_query(select_posts)

        for post in posts:
            print(post)
            
            
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"file_name"
    # описание столбцов словаря - id номер, слово и значение
    sql_create_dictionary_table = """ CREATE TABLE IF NOT EXISTS dictionary (
                                        id integer PRIMARY KEY,
                                        word text,
                                        meaning text
                                    ); """

    # подключение к базе
    conn = create_connection(database)

    # создание таблицы dictionary
    if conn is not None:
        create_table(conn, sql_create_dictionary_table)
    else:
        print("Ошибка: не удалось подключиться к базе.")


if __name__ == '__main__':
    main()


def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()

    # запрос на извлечение всех существующих записей из базы в алфавитном порядке
def get_words(self):
        query = 'SELECT * FROM dictionary ORDER BY word DESC'
        db_rows = self.run_query(query)
        # формирование словаря из перемешанных в случайном порядке слов и их значений
        lst_left, lst_right = [], []
    for row in db_rows:
            lst_left.append(row[1])
            lst_right.append(row[2])
        random.shuffle(lst_left)
        random.shuffle(lst_right)
        dic = dict(zip(lst_left, lst_right))