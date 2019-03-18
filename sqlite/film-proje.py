from film import *

print("""***********************************

Film Arþiv Programýna Hoþgeldiniz.

Ýþlemler;

1. Filmleri Göster

2. Film Sorgulama

3. Film Ekle

4. Film Sil 

5. Filmin türünü deðiþtir

Çýkmak için 'q' ya basýn.
***********************************""")

film = Arsiv()

while True:
    islem = input("Yapýlacak iþlemi seçiniz:")
    if islem == "q":
        print("Programdan çýkýlýyor...")
        break

    if islem == "1":
        film.filmleri_goster()

    if islem == "2":
        islem2 = input("Aradýðýnýz filmin adýný yazýnýz: ")

        print("Film sorgulanýyor.....")
        time.sleep(1)
        film.film_sorgula(islem2)


    if islem == "3":
        film_ismi = input("Film Ismi: ")
        yonetmen = input("Yönetmen: ")
        tur = input("Film Türü: ")
        sure = input("Filmin Süresi: ")
        yapimci = input("Yapýmcý: ")

        yeni_film = Film(film_ismi,yonetmen,tur,sure,yapimci)
        print("Film ekleniyor....")
        time.sleep(1)
        film.film_ekle(yeni_film)
        print("Film eklendi....")


    if islem == "4":
        silinecek_film = input("Silinecek filmin adýný giriniz: ")

        film.film_sil(silinecek_film)


    if islem == "5":
        eski_film = input("Türünü güncellemek istediðiniz filmi giriniz: ")
        yeni_tur = input("Filmin yeni türünü giriniz: ")

        print("Film güncelleniyor....")
        time.sleep(1)
        film.tur_guncelle(eski_film,yeni_tur)
        print("Film guncellendi........")


