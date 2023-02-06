import sqlite3
conn  =  sqlite3.connect ( 'Bootcamp2023.db' )
def get_onbranch(input_branch):
    records = conn.execute("select *from Participants where branch='"+str(input_branch)+"'")
    for i in records:
        print(i)
    conn.commit()