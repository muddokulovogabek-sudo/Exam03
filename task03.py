file = open("data.txt", "r")

foydalanuvchilar = len(file.readlines())

print("Foydalanuvchilar soni:", foydalanuvchilar)

file.close()
