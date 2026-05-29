import json

yangi_foydalanuvchi = {
    "id": 3,
    "ism": "Ali",
    "yosh": 22
}

with open("data.json", "r") as fayl:
    malumotlar = json.load(fayl)

malumotlar.append(yangi_foydalanuvchi)

with open("data.json", "w") as fayl:
    json.dump(malumotlar, fayl, indent=4)

print("Foydalanuvchi JSON faylga qo‘shildi!")