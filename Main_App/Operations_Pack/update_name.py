import sqlite3
conn  =  sqlite3.connect ( 'Bootcamp2023.db' )
def update(g_id,new_name):
    conn.execute("update participants set name='"+str(new_name)+"' where g_id='"+str(g_id)+"'")
    conn.commit()