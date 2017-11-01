import json


filename = 'num.json'
with open(filename) as f_obj:
    data = json.load(f_obj)
    print("I know your favorite number! It's " + data + ".")