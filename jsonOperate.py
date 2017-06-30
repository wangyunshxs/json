import json
import time

def store(data):
    with open('data/jsonOperate.json', 'w') as json_file:
        json_file.write(json.dumps(data))

def load():
    with open('data/jsonOperate.json',mode ="r") as json_file:
        data = json.load(json_file,encoding="utf-8")
        return data

if __name__ == "__main__":
    data = {}
    data["last"]=time.strftime("%Y%m%d")
    store(data)
    data = load()
    print data

