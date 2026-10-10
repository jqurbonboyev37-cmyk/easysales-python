
print("===== EasySales =====")

jami = 0

while True:
    mahsulot = input("Mahsulot nomi (tugatish uchun exit): ")

    if mahsulot.lower() == "exit":
        break

    try:
        narx = float(input("Mahsulot narxi: "))
        soni = int(input("Mahsulot soni: "))

        if narx < 0 or soni < 0:
            print("Manfiy qiymat kiritmang!")
            continue

        summa = narx * soni
        jami += summa

        print("Mahsulot summasi:", summa)
        print("Jami savdo:", jami)

    except ValueError:
        print("Iltimos, raqam kiriting!")

with open("hisobot.txt", "w", encoding="utf-8") as fayl:
    fayl.write(f"Bugungi jami savdo: {jami}\n")

print("Hisobot saqlandi!")
print("Jami savdo:", jami)
