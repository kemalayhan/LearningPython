class Çalışan():

    def __init__(self,isim, maaş, departman):
        print("Çalışan sınıfı init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgileri_goster(self):
        print("İsim: {} \nMaaş: {} \nDepartman: {} ".format(self.isim,self.maaş,self.departman))

class Yönetici(Çalışan):
    def __init__(self,isim, maaş, departman, kişi_sayısı):
        super().__init__(isim, maaş, departman)
        print("Yönetici Sınıfı init fonksiyonu")

        self.kişi_sayısı = kişi_sayısı

    def bilgileri_goster(self):
        print("Yönetici sınıfının bilgileri.....")

        print(
        "İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim, self.maaş, self.departman, self.kişi_sayısı))
    def zam_yap(self,zam):
        self.maaş += zam

yönetici = Yönetici("kemal", 5000, "bilişim", 10)
yönetici.zam_yap(2000)
yönetici.bilgileri_goster()
