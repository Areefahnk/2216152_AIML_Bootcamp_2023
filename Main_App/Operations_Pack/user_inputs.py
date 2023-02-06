import sqlite3
conn  =  sqlite3.connect ( 'Bootcamp2023.db' )
def input_data():
    data={}
    g_id = int(input("Enter G_id:"))
    name = input("Enter Name:")
    branch = input("Enter Branch:")
    study = input("Enter the Study:")
    data["g_id"]=g_id
    data["name"]=name
    data["branch"]=branch
    data["study"]=study
    conn.execute('''
    insert into participants(G_id,name,branch,study) Values(?,?,?,?)
    ''',(data.get("g_id"),data.get("name"),data.get("branch"),data.get("study")))

    conn.commit()
    print('Data entered successfully.')
    return data



