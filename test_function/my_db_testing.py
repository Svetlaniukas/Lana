from ast import Attribute
from platform import node
import sqlite3


def work_with_sql_lite_db_files(file_db, key_name, val_name):
    db_dict = {}
    try:
        con = sqlite3.connect()
        con.row_factory = sqlite3.Row
        data = file_db.fetchall()
        for key_name, val_name in con:
            keys = con.keys()
                for keys in con.row_factory:
                    if key_name in Attribute and val_name Attribute:
                    key = node.attr[key_name]
                    val = sqlite3.Row.attr[val_name]
                    db_dict[key] = val
    except AssertionError:
        print('exceptation')
    return db_dict
