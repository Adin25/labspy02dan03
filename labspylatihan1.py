angka1 = int(input("masukan bilangan pertama: "))
angka2 = int(input("masukan bilangan kedua: "))
angka3 = int(input("masukan bilangan ketiga: "))

if angka1 > angka2 > angka3:
    print("bilangan pertama adalah bilangan terbesar")
elif angka2 > angka3:
    print("bilangan kedua adalah bilangan terbesar")
else:
    print("bilangan ketiga adalah bilangan terbesar")