import random, time

print("""
******************

Sayı Tahmin Oyunu

Tahmin 0 - 40 arasında olmalı
******************
""")


n = random.randint(0,40)
hak = 7

while hak > 0:
    tahmin = int(input("Tahmininizi giriniz:"))

    if tahmin > n:
        print("Tahmin Sorgulanıyor")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin")
        hak -= 1

    elif tahmin < n:
        print("Tahmin Sorgulanıyor")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin")
        hak -= 1

    else:
        print("Tahmin Sorgulanıyor")
        time.sleep(1)
        print("Doğru tahmin")
        break

