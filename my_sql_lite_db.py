import sqlite3

shift = [
         ("Monday", "10.am-4.pm"),
         ("Tuesday", "9.am-3.pm"),
         ("Wednesday", "10.am-5.pm"),
         ("Thursday", "10am-4pm"),
         ("Friday", "8am-4pm")


         ("Saturday", "10.am-5.pm"),
         ("Sunday", "8am- 4pm")

]
with sqlite3.connect("staff_shift.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS user")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT,
        time_sfift INTEGER
       )""")
    for shift in shift:
        cur.execute("INSERT INTO time_table VALUES(NULL, ?, ?)", shift)
