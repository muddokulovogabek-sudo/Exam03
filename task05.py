import json

try:
    file = open("data.json", "r")
    data = json.load(file)

    for user in data:
        print("Name:", user["Name"], ", Age:", user["Age"])

    file.close()

except:
    print("Fayl topilmadi!")