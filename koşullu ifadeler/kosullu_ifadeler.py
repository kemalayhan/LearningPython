#3 sayıdan en büyüğü bulan prog
a = int(input("1. Sayıyı giriniz:"))
b = int(input("2. Sayıyı giriniz:"))
c = int(input("3. Sayıyı giriniz:"))

if a > b and a > c:
    print("En büyük sayı:",a)
elif b > a and b > c:
    print("En büyük sayı:",b)
elif c > a and c > b:
    print("En büyük sayı:",c)

#3 nottan ortalamasını alıp harf notuna çeviren prog

vize1 = int(input("1. vizeyi girin:")) * 30 / 100
vize2 = int(input("2. vizeyi girin:")) * 30 / 100
fnl = int(input("Final notunu girin:")) * 40 / 100
sonuc = vize1 + vize2 + fnl

if (sonuc>= 90):
    print("AA")
elif (sonuc >= 85):
    print("BA")
elif (sonuc >= 80):
    print("BB")
elif (sonuc >= 75):
    print("CB")
elif (sonuc >= 70):
    print("CC")
elif (sonuc >= 65):
    print("DC")
elif (sonuc >= 60):
    print("DD")
elif (sonuc >= 55):
    print("FD")
else:
    print("FF")

# girilen geometrik şekli detaylandıran prog
sekil = input("Geometrik şekil yazınız:")
if sekil == "üçgen":
    kenar1 = int(input("İlk kenarı giriniz:"))
    kenar2 = int(input("İkinci kenarı giriniz:"))
    kenar3 = int(input("Üçüncü kenarı giriniz:"))
    if kenar1 + kenar2 > kenar3 and kenar1 + kenar3 > kenar2 and kenar2 + kenar3 > kenar1:
        if kenar1 == kenar2 and kenar1 == kenar3:
            print("Eşkenar üçgen")
        elif (kenar1 == kenar2 and kenar1 != kenar3) or (kenar2 == kenar3 and kenar2 != kenar1) or (kenar1 == kenar3 and kenar2 != kenar1):
            print("İkiz kenar üçgen")
        else:
            print("Çeşit kenar üçgen")
    else:
        print("Üçgen değil")
elif sekil == "dörtgen":
    kenar1 = int(input("İlk kenarı giriniz:"))
    kenar2 = int(input("İkinci kenarı giriniz:"))
    kenar3 = int(input("Üçüncü kenarı giriniz:"))
    kenar4 = int(input("Dördüncü kenarı giriniz:"))
    if (kenar1 == kenar2) and (kenar1 == kenar3) and (kenar1 == kenar4):
        print("Şekil kare:")
    elif (kenar1 == kenar3) and (kenar2 == kenar4):
        print("Şekil Dikdörtgen")
    else:
        print("Şekil dörtgen")
else:
    print("Geçersiz Şekil")
