class Hayvan():
    def __init__(self, isim, ort_yaşam, hız, üreme, popülasyon):
        self.isim = isim
        self.ort_yaşam = ort_yaşam
        self.hız = hız
        self.üreme = üreme
        self.popülasyon = popülasyon
    def __str__(self):
        return "isim: {}\nOrtamala Yaşam Süresi: {}\nHız: {}\nÜreme: {}\nPopülasyon = {}".format(self.isim,self.ort_yaşam,self.hız,self.üreme,self.popülasyon)
    def __len__(self):
        return self.popülasyon

class Aslan(Hayvan):
    def __init__(self,isim, ort_yaşam, hız, üreme, popülasyon, vasıf):
        super().__init__(isim, ort_yaşam, hız, üreme, popülasyon)
        self.vasıf = vasıf

    def kral(self):
        print("Ormanların kralı aslandır.")

class Kartal(Hayvan):
    def __init__(self, isim, ort_yaşam, hız, üreme, popülasyon, kanat):
        super().__init__(isim, ort_yaşam, hız, üreme, popülasyon)
        self.kanat = kanat
    def uç(self):
        print("Kartallar yüksekten uçar.")

class At(Hayvan):
    def __init__(self, isim, ort_yaşam, hız, üreme, popülasyon, vefa):
        super().__init__(isim, ort_yaşam, hız, üreme, popülasyon)
        self.vefa = vefa

    def koş(self):
        print("Atlar çok hızlı koşar.")

class Kanguru(Hayvan):
    def __init__(self, isim, ort_yaşam, hız, üreme, popülasyon, yetenek):
        super().__init__(isim, ort_yaşam, hız, üreme, popülasyon)
        self.yetenek = yetenek

    def vur(self):
        return "Kangurular yumruk atabilir."

aslan = Aslan("Kral Faruk", 30, 50, "Eşeyli", 1000, "Kral")
aslan.kral()

kartal = Kartal("Yalnız Recep", 50, 200,"Yumurtlayarak", 2000, "Kanatları var")
kartal.uç()

at = At("Melek Sabri", 40, 150, "Eşeyli", 1500, "Sadık")
at.koş()

kanguru = Kanguru("Beton Ziya", 30, 60, "Bilmiyorum", 2000, "Boksör")
print(kanguru.vur())