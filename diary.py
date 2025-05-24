import json
import os
import time

"""
create
read
update
delete
menu
quit
"""
DATA_FILE = "public\data-example.json"


def load_data(): # load data.json
    decoded:list = []
    with open(DATA_FILE, "r") as file:
        try:
            decoded = json.load(file.read())
        except json.JSONDecodeError:
            decoded = []
            raise json.JSONDecodeError
    # print(decoded)
    # while True:
    #     print(eval(input("debug: ")))

    return decoded

def write():
    os.system("cls")

    title = input("title: ")
    date = rf"{time.localtime().tm_year}/{time.localtime().tm_mon}/{time.localtime().tm_mday}"
    with open("public\counter.txt", "r") as file:
        id = file.read()
    path = rf"private\diary\{id}.txt"
    temp_object = {
        "title": title,
        "date": date,
        "id": id,
        "path": path
    }
    with open(DATA_FILE, "w+") as file:
        decoded = load_data()
        decoded.append(str(temp_object))
        print(decoded)
        # file.write(json.dumps(decoded))
        




    

def menu():
    os.system("cls")
    interface = """
    write (w)
    read (r)
    modify (m)
    delete (d)
    quit (quit)
    """

    print(f"{interface}\n=============================================")
    cmd = input("cmd: ")

    match cmd:
        case "w":
            write()
        # case "r":
        #     read()
        # case "m":
        #     modify()
        # case "d":
        #     delete()
        # case "quit":
        #     quit()

menu()