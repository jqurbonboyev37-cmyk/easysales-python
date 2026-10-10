print("===== EasySales 2.0 =====")

jami = 0
mahsulotlar = []

while True:
    mahsulot = input("Mahsulot nomi (exit — tugatish): ")

    if mahsulot.lower() == "exit":
        break

    try:
        narx = float(input("Mahsulot narxi: "))
        soni = int(input("Mahsulot soni: "))

        if narx < 0 or soni <= 0:
            print("Narx manfiy bo‘lmasin, soni esa 0 dan katta bo‘lsin!")
            continue

        summa = narx * soni
        jami += summa

        mahsulotlar.append(
            f"{mahsulot}: {soni} dona × {narx} = {summa}"
        )

        print("Mahsulot summasi:", summa)
        print("Jami savdo:", jami)

    except ValueError:
        print("Iltimos, to‘g‘ri raqam kiriting!")

with open("hisobot.txt", "w", encoding="utf-8") as fayl:
    fayl.write("===== EasySales hisoboti =====\n")

    for mahsulot in mahsulotlar:
        fayl.write(mahsulot + "\n")

    fayl.write(f"\nJami savdo: {jami}\n")

print("Hisobot saqlandi!")
print("Jami savdo:", jami)
print("EasySales dasturidan foydalanganingiz uchun rahmat!")
print("Dastur versiyasi: 2.0")
