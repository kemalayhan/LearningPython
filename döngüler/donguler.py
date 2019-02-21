#Mükemmel sayıyı bulan sayı
sayi = int(input("Bir sayı giriniz:"))
toplam = 0
i = 1
for i in range(1,sayi):
    if sayi % i == 0:
        toplam += i


if toplam == sayi:
    print("seçtiğiniz sayı mükemmel")
else:
    print("Mükemmel olmayan sayı seçtiniz")

#1- 100, 3'e bölünen sayılar
i = 0
while (i <= 100):
    i += 1
    if (i % 3 != 0):
        continue
    print(i)




#Çarpım tablosu

for i in range(1, 11):
    print("*************************************************")
    for j in range(1, 11):
        print("{} x {} = {}".format(i, j, i * j))

#Armstrong sayı bulan prog

sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    basamak = gecici_sayı % 10

    toplam += basamak ** basamak_sayisi

    gecici_sayı //= 10

if (toplam == sayı):
    print(sayı, "bir armstrong sayısıdır.")
else:
    print(sayı, "bir armstrong sayısı değildir.")

#girdiğiniz sayıların q' ya basınca yazan prog

toplam = 0
while True:
    sayi = input("Bir sayı giriniz:")
    if (sayi == "q"):
        print("programdan çıkılıyor")

        break
    sayi = int(sayi)
    toplam += sayi
print("girdiğiniz sayıların toplamı:",toplam)

#1-100 arası 2'ye bölünen sayılar

liste1 = [i for i in (range(0,101)) if (i % 2 == 0)]
print(liste1)
