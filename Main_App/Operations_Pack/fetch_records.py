import sqlite3
conn  =  sqlite3.connect ( 'Bootcamp2023.db' )
def get_records():
    records = conn.execute("select *from Participants")
    for i in records:
        print(i)
    conn.commit()