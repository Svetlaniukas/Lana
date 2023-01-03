
import sqlite3


def work_with_sql_lite_db_files(file_name, key_name, val_name):
    db_dict = {}
    con = sqlite3.connect(file_name)
    try:
        con.row_factory = sqlite3.Row
        db_dict = con.cursor()
        for keys in db_dict:
            dict = db_dict.execute()
            if keys not in dict():
                return{}
    except AssertionError:
        print('exceptation')
    return keys.fromkeys()






def work_with_sql_lite_db_files(file, key_name, val_name):
    con = sqlite3.connect(file)
    con.row_factory = sqlite3.Row
    data = con.fetchall()
    for result in data:
        return result[key_name], result[val_name]
