class Kahraman():
    def __init__(self, takma_isim = "Süperman", isim="Clark", meslek="gazeteci", maaş=2000, şirket="DC", pelerin = "yok"):
        self.takma_isim = takma_isim
        self.isim = isim
        self.meslek = meslek
        self.maaş = maaş
        self.şirket = şirket
        self.pelerin = pelerin

    def pelerin_ver(self):
        self.pelerin = "var"

    def takma_isim_degis(self, yti):
        self.takma_isim = yti

    def isim_degis(self, yi):
        self.isim = yi

    def meslek_degis(self,ym):
        self.meslek = ym

    def maas_dusur_arttır(self):
        while True:
            miktar = (input("Maaşı düşürmek için '-'değer, arttırmak için '+' değer giriniz."))
            if (miktar == "q"):
                break
            miktar = int(miktar)
            if (miktar == "0"):
                print("Değişiklik yapılmadı",self.maaş)
            else:
                self.maaş += miktar
                print("Maaş:", self.maaş)

                print("Maaş Güncellendi:", self.maaş)
                break

    def __str__(self):
        return """
        Takma İsim: {}
        İsim: {}
        Meslek: {}
        Maaş: {}
        Şirket: {}
        Pelerin: {}
        """.format(self.takma_isim,self.isim,self.meslek,self.maaş,self.şirket,self.pelerin)

    def __len__(self):
        return kahraman.maaş

kahraman = Kahraman()

print("""
******************
Süper kahraman 
1. Kahraman Bilgileri
2. Takma isim değiştir
3. İsim değiştir
4. Meslek değiştir
5. Maaş arttır-azalt
Çıkmak için 'q' ya bas.
""")
print("Başlangıçtaki Maaş:",len(kahraman))
while True:
    i = input("İşlem seçiniz: ")
    if (i == "q"):
        print("Programdan çıkılıyor")
        break
    elif (i == "1"):
        print("Kahraman Bilgileri:\n",kahraman)
    elif (i == "2"):
        yti = input("Yeni takma isim giriniz:")
        kahraman.takma_isim_degis(yti)
        print(kahraman.takma_isim," yeni takma isim olmuştur")
    elif (i == "3"):
        yi = input("Yeni isim giriniz:")
        kahraman.isim_degis(yi)
        print(kahraman.isim," yeni isim olmuştur")
    elif (i == "4"):
        ym = input("Yeni meslek giriniz:")
        kahraman.meslek_degis(ym)
        print(kahraman.meslek," yeni meslek olmuştur")
    elif (i == "5"):
        kahraman.maas_dusur_arttır()
    else:
        print("Geçersiz işlem")
