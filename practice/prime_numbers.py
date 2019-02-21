def is_prime(numb):
    if numb == 1:
        return False
    elif numb == 2:
        return True

    else:
        for i in range(2,numb):
            if (numb % i == 0):
                return False
        return True

while True:
    numb = (input("Kontrol edeceğiniz sayıyı giriniz:"))

    if numb == "q":
        print("Programdan çıkılıyor")
        break
    else:
        numb = int(numb)
        if is_prime(numb):
            print(numb, "Asal bir sayı")
        else:
            print(numb, "Asal bir sayı değil")
