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
    try:
        data = json.load(open("database.json"))
        data.pop(["cases"][str(case_id)], open("database.json", "w"))
    except KeyError:
        raise "Oh no! Looks like this case doesn't exist!"

def delete(case_id:int):
    remove(case_id)

def display(case_id:int):
    try:
        data = json.load(open("database.json"))
        return data["cases"][str(case_id)]
    except KeyError:
        print("Oh no! Looks like this case doesn't exist!")

def edit(case_id:int, new_text:str):
    try:
        data = json.load(open("database.json"))
        data["cases"][str(case_id)] = new_text
        json.dump(data, open("database.json", "w"))
    except KeyError:
        print("Oh no! Looks like this case doesn't exist!")
