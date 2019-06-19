#1-1000 mükemmel sayıları fonksiyon
def mukemmel():
    toplam = 0
    liste = []

    for i in range(1,1000):
        for j in range(1,i):
            if i % j == 0:
                toplam += j
        if toplam == i:
            liste.append(i)
        toplam = 0
    print(liste)

mukemmel()


#Kullanıcının girdiği 2 sayının ebobu
def ebob(sayi1,sayi2):

    ebob = 1
    for i in range(1,sayi1):
        if (not sayi1 % i and not sayi2 % i):
            ebob = i
    return ebob

a = ebob(25,55)
print(a)


#Kullanıcının girdiği 2 sayının ekoku
def ekok(sayi1, sayi2):
    i = 2
    ekok = 1

    while True:
        if (sayi1 % i == 0 and sayi2 % i == 0):
            sayi1 /= i
            sayi2 /= i
            ekok *= i

        elif (sayi1 % i == 0 and sayi2 % i != 0):
            sayi1 /= i
            ekok *= i

        elif (sayi1 % i != 0 and sayi2 % i == 0):
            sayi2 /= i
            ekok *= i
        else:
            i +=1
        if (sayi1 == 1 and sayi2 == 1):
            break
    return ekok

print(ekok(5,6))

#Kullanıcının girdiği 2 basamaklı sayının okunusu
def okunus(sayi):
    birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
    s_onlar = sayi // 10
    s_birler = sayi % 10
    return onlar[s_onlar] + " " + birler[s_birler]

print(okunus(23))

#Pisagor üçgenleri
def pisagor_bul():
    pisagor_liste = list()
    for i in range(0,101):
        for j in range(0,101):
            c = (j ** 2 + i ** 2) ** 0.5
            if(c == int(c)):
                pisagor_liste.append((i, j, int(c)))
    return pisagor_liste


for i in pisagor_bul():
    print(i)
	
#Bilgileri Yazdırma
	def ogrenci(*bilgiler):
    bilgi = ""
    for i in bilgiler:
        bilgi += i
    print("Ögrencinin bilgileri:\n", bilgi)


ogrenci("Mazlum ", "Teknoloji Fakütesi ", "Bilgisayar Mühendisliği ", "1.Sınıf")