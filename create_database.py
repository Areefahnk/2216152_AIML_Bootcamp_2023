#Steps:
'''
1. importing the module
2. Create a database
3. Connecting to the database
4. Create a table in the database - write a query
5. Executing a query
'''
#step 1
import sqlite3
#step 2
"Bootcamp2023.db"
#step 3 - connect a database
conn=sqlite3.connect("Bootcamp2023.db")
print(conn)

#step 4
'''
create table table_name(column_name1 datatype constraints,column_name2 datatype constraints,.........)

constraints -> primary key, not null, unique,.... ->optional
'''

query = '''
        create table Participants(G_id int primary key,Name text not null,Branch text not null,Study text not null DEFAULT 'BTech')
        '''
conn.execute(query)





#query='''create table Participants(G_id int primary key,Name text not null,Branch text not null,Study text not null,
#            status text DEFAULT 'Registered')

#Study - 1 year, 2 year and I wanted BTech, MSc..


