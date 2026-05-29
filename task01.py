ism = input("Ism kiriting: ")
yosh = input("Yosh kiriting: ")

fayl = open("data.txt", "a")

fayl.write(ism + " – " + yosh)

fayl.close()

print(f"{ism} - {yosh} yosh")