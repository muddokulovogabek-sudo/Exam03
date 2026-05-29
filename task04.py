import json

name = input("Ism: ")
age = int(input("Yosh: "))

new_user = {"name": name, "age": age}

try:
    with open("data.json", "r") as f:
        data = json.load(f)
except:
    data = []

data.append(new_user)

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Saqlanldi")