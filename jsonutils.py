import json

FILE_NAME="data/stud.json"

def read_json():
    with open(FILE_NAME) as f:
        data=json.load(f)
    return data

def write_json(data):
    with open(FILE_NAME,"w") as f:
        json.dump(data,f,indent=3)