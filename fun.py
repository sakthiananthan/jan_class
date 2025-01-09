from jsonutils import *

def register_stud(name,age,course,address):
    data=read_json()
    temp_dict={
        "sno": len(data["students"])+1,
        "name":name,
        "Age":age,
        "course":course,
        "address":address
    }
    data['students'].append(temp_dict)
    write_json(data)
    

def update_stud(id,name,age,course,address):
    data=read_json()
    for stud in data["students"]:
        if str(stud["sno"]) == id:
            stud["name"]=name
            stud["Age"]=age
            stud["course"]=course
            stud["address"]=address
            break
    write_json(data)
            
def delete_stud(id):
    # print(id)
    data=read_json()
    for stud in data["students"]:
        if str(stud["sno"]) == id:
            print(stud)
            data["students"].remove(stud)
            break
    i=1
    for stud in data['students']:
        stud["sno"]=i
        i+=1
    write_json(data)
    