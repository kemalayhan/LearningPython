def hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    final = int(liste[3])
    son_not = not1 * (3 / 10) + not2 * (3 / 10) + final * (4 / 10)
    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"
    return isim + "-------->" + harf + "\n"


def gec_kal(satir):
    satir = satir[:-1]
    liste = satir.split("-------->")
    isim = liste[0]
    harf = liste[1]
    if harf == "FF":
        return True
    else:
        return False


with open("notlar.txt", "r") as file:
    eklenecekler = []
    for i in file:
        eklenecekler.append(hesapla(i))

    with open("son_notlar.txt", "w", encoding="utf-8") as file2:
        for i in eklenecekler:
            file2.write(i)

with open("son_notlar.txt", "r", encoding="utf-8") as file3:
    gecenler = []
    kalanlar = []
    for i in file3:
        if gec_kal(i):
            kalanlar.append(i)
        else:
            gecenler.append(i)
    with open("gecenler.txt", "w", encoding="utf-8") as file4:
        for i in gecenler:
            file4.write(i)
    with open("kalanlar.txt", "w", encoding="utf-8") as file5:
        for i in kalanlar:
            file5.write(i)
