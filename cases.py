import json

def count():
    data = json.load(open("database.json"))
    return data["next_case"]

def create(text:str):
    data = json.load(open("database.json"))
    data["cases"][data["next_case"]] = text
    addItem = int(data["next_case"]) +1
    data["next_case"] = str(addItem)
    json.dump(data, open("database.json", "w"))

def remove(case_id:int):
    data = json.load(open("database.json"))
    data["cases"][str(case_id)] = None
    json.dump(data, open("database.json", "w"))

def delete(case_id:int):
    remove(case_id)

def display(case_id:int):
    data = json.load(open("database.json"))
    return data["cases"][str(case_id)]

def edit(case_id:int, new_text:str):
    data = json.load(open("database.json"))
    data["cases"][str(case_id)] = new_text
    json.dump(data, open("database.json", "w"))
