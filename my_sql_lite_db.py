import sqlite3
from sqlite3 import Error


time_table = [
         ("Monday", "10.am-4.pm"),
         ("Tuesday", "9.am-3.pm"),
         ("Wednesday", "10.am-5.pm"),
         ("Thursday", "10am-4pm"),
         ("Friday", "8am-4pm"),


         ("Saturday", "10.am-5.pm"),
         ("Sunday", "8am- 4pm")

]

con = sqlite3.connect("staff_shift.db")
try:
    cur = con.cursor()
    cur.execute("SELECT * FROM time_table")
    print(cur.fetchall())
    print('test')

    cur.execute("DROP TABLE IF EXISTS time_table")
    cur.execute("""CREATE TABLE IF NOT EXISTS time_table (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT,
        time_sfift TEXT
    )""")
    for shift in time_table:
        cur.execute("INSERT INTO time_table VALUES(NULL, ?, ?)", shift)

    cur.execute("SELECT * FROM time_table")
    print(cur.fetchall())
    cur.close()
    con.commit()

except Error as e:
    if con:
        con.rollback()
    print("not found object", e)
con.close()
