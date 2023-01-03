
import sqlite3


def work_with_sql_lite_db_files(file_db, key_name, val_name):
    db_dict = {}
    try:
        con = sqlite3.connect('staff_sfift.db')
        con.row_factory = sqlite3.Row
        data = file_db.fetchall()
        for sqlite3.Row.keys in data:
            if key_name in data and val_name in data():
                key = [key_name]
                val = [val_name]
                db_dict[key] = val
    except AssertionError:
        print('exceptation')
    return db_dict
