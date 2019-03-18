import sqlite3

import time

class Film():

    def __init__(self,isim,yonetmen,tur,sure,yapimci):

        self.isim = isim
        self.yonetmen = yonetmen
        self.tur = tur
        self.sure = sure
        self.yapimci = yapimci

    def __str__(self):

        return "Film: {}\nYönetmen: {}\nTür: {}\nSüre: {}\nYapýmcý:{}".format(self.isim,self.yonetmen,self.tur,self.sure,self.yapimci)

class Arsiv():

    def __init__(self):
        self.baglanti_olustur()


    def baglanti_olustur(self):
        self.con = sqlite3.connect("arsiv.db")

        self.cursor = self.con.cursor()

        sorgu = "Create Table If Not Exists filmler (film TEXT,yonetmen TEXT,tur TEXT,sure INT,yapimci TEXT)"
        self.cursor.execute(sorgu)
        self.con.commit()


    def baglanti_kes(self):
        self.con.close()


    def filmleri_goster(self):
        sorgu = "Select * from filmler"
        self.cursor.execute(sorgu)
        filmler = self.cursor.fetchall()

        if len(filmler) == 0:
            print("Arþivde hiç film bulunmamaktadýr....")

        else:
            for i in filmler:
                film = Film(i[0],i[1],i[2],i[3],i[4])
                print(film)


    def film_sorgula(self,film):
        sorgu = "Select * from filmler where film = ?"
        self.cursor.execute(sorgu,(film,))
        filmler = self.cursor.fetchall()

        if len(filmler) == 0:
            print("Aradýðýnýz film bulunmamaktadýr....")

        else:
            for i in filmler:
                film = Film(i[0],i[1],i[2],i[3],i[4])
                print(film)


    def film_ekle(self,film):

        sorgu = "Insert into filmler Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(film.isim,film.yonetmen,film.tur,film.sure,film.yapimci))
        self.con.commit()


    def film_sil(self,film):
        sorgu = "Delete from filmler where film = ?"

        self.cursor.execute(sorgu,(film,))
        self.con.commit()


    def tur_guncelle(self,eski_film,yeni_tur):
        sorgu = "Select * from filmler where film = ?"

        self.cursor.execute(sorgu,(eski_film,))

        filmler = self.cursor.fetchall()

        if len(filmler) == 0:
            print("Aradýðýnýz film bulunmamaktadýr....")
            print("1. Ýþlem ile filmleri görüntüleyip tekrar seçiniz....")

        else:
            sorgu2= "Update filmler set tur = ? where film = ?"

            self.cursor.execute(sorgu2,(yeni_tur,eski_film))

            self.con.commit()






