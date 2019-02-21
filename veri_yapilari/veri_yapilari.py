#kullanıcının girdiği 3 sayıyı çarpan prog
a = int(input("1. Sayıyı giriniz:"))
b = int(input("2. Sayıyı giriniz:"))
c = int(input("3. Sayıyı giriniz:"))
print("{}, {} ve {}'nın çarpımı {}'e eşit.".format(a,b,c,a*b*c))

#Beden kitle indeksi bulan prog
boy = float(input("Boyunuzu yazınız:"))
kilo = float(input("Kilonuzu yazınız:"))
indeks = kilo/(boy**2)
print("Beden kitle indeksiniz: {}'e eşit".format(indeks))

#Kullanıcının alınan iki sayının yerinin degistiren prog
a = input("1. sayıyı giriniz:")
b = input("2. sayıyı giriniz:")
a,b = b,a
print(a,b,sep="/")

#Dik kenarları verilen üçgenin hipo bulma
dkenar1 = int(input("a:"))
dkenar2 = int(input("b:"))
hipo = (dkenar1 ** 2 + dkenar2 ** 2) ** 0.5
print("Hipotenüs=",hipo)