
import sqlite3


def work_with_sql_lite_db_files(file_name, key_name, val_name):
    db_dict = {}
    try:
        con = sqlite3.connect('staft_shift.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        for keys in cur:
            dict = cur.execute()
            if key_name in dict and val_name in dict():
                key = keys[key_name]
                val = keys[val_name]
                db_dict[key] = val
    except AssertionError:
        print('exceptation')
    return db_dict






def work1_with_sql_lite_db_files(key_name, val_name):
    db_dict = {}
    try:
        con = sqlite3.connect('staff_sfift.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        for keys in cur:
            if key_name and val_name in cur():
                key = keys[key_name]
                val = keys[val_name]
                db_dict[key] = val
    except AssertionError:
        print('exceptation')
    return db_dict
