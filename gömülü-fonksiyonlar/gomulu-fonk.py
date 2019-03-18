from functools import reduce

#dikdörtgen alan bulma
def alanbul(tuple):
    return tuple[0] * tuple[1]

dikdörtgen = [(3,4),(10,3),(5,6),(1,9)]

print(list(map(alanbul, dikdörtgen)))

#ucgen mi degil mi
def ucgen_mi(kenar):
    if (kenar[0] + kenar[1] > kenar[2] and kenar[0] + kenar[2] > kenar[1] and kenar[2] + kenar[1] > kenar[0]):
        return True
    else:
        return False

ucgen = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(ucgen_mi, ucgen)))

#Çift sayıları topla
def cift_mi(x):
    return not x % 2

cift_sayilar = list(filter(cift_mi, range(1,11)))
print(reduce(lambda x,y : x + y, cift_sayilar))

#zip fonksiyonu
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
isim_soyisim = list(zip(isimler,soyisimler))
for i,j in isim_soyisim:
    print(i, j)