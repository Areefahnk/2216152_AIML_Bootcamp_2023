from Main_App.Operations_Pack import user_inputs as u
from Main_App.Operations_Pack import fetch_records as f
from Main_App.Operations_Pack import fetch_on_branch as b
from Main_App.Operations_Pack import update_name as n
while True:
    print('''1. Enter Participant Details
    2. Fetch the Participant details
    3. Fetch participants based on Branch only 
    4. Update wrongly entered name change based on G_id
    5. exit''')
    print("Choose any option from above menu:")
    ch = int(input())
    if ch == 1:
        print(u.input_data())
    elif ch==2:
        f.get_records()
    elif ch==3:
        input_branch=input("Enter Branch in caps:")
        b.get_onbranch(input_branch)
    elif ch==4:
        id=int(input("Enter you id:"))
        new_name=input("Enter new name to be updated")
        n.update(id,new_name)
    else:
        break