import random
import time

class Kumanda():


    def __init__(self,tv_durum = "Kapalı",tv_ses = 6,kanal_listesi = ["BBC"],kanal = "BBC"):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

    def tv_ac(self):

        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık....")
        else:
            print("Televizyon Açılıyor...")
            self.tv_durum  = "Açık"

    def tv_kapat(self):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon Zaten Kapalı..")
        else:
            print("Televizyon Kapanıyor....")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):

        while True:
            cevap =  input("Sesize Al: M \nSesi Azalt: '<'\nSesi Artır: '>'\nÇıkış : çıkış\n")

            if (cevap == "M"):
                self.tv_ses = 0
                print("TV Sesize alindi")
            elif (cevap == "<"):
                if (self.tv_ses != 0):

                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
                else:
                    print("Ses: 0 - En dusuk Ses")
            elif (cevap == ">"):
                if (self.tv_ses != 31):

                    self.tv_ses += 1

                    print("Ses:",self.tv_ses)
                else:
                    print("Ses: 31 - En yuksek Ses")
            else:
                print("Ses Güncellendi:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):

        print("Kanal ekleniyor....")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal Eklendi.....")
    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)


        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki Kanal:" ,self.kanal)


    def tv_cal(self):

        # PS: To run this code need to remove triple quotes from print below.
        print("""-------------------------------------------------
        Hesap Makinesi Programına Hoşgeldiniz
        İşlemler;

        1. Toplama İşlemi

        2. Çıkarma İşlemi

        3. Çarpma İşlemi

        4. Bölme İşlemi

        Çıkmak için 'q' ya basın.

        -----------------------------------------------------------
        """)

        işlem =  input("İşlem Numarasını Giriniz:") # Buna göre koşullarımızı yazacağız.

        if (işlem == "q"):
            print("Program Sonlandırılıyor...")

        else:

            a = float(input("Birinci Sayı:")) # Birinci Sayıyı Alıyoruz.
            b = float(input("İkinci Sayı:")) # İkinci Sayıyı Alıyoruz.

            if (işlem == "1"): # Toplama İşlemi
                print("{} ile {} 'nin toplamı {} dır.".format(a,b,a+b))

            elif (işlem == "2"):
                print("{} ile {} 'nin farkı {} dır.".format(a, b, a - b))

            elif (işlem == "3"):
                print("{} ile {} 'nin çarpımı {} dır.".format(a, b, a * b))

            elif (işlem == "4"):
                print("{} 'nın {} 'e bölümü {} dır.".format(a, b, a / b))

            else:
                print("Lütfen geçerli bir işlem giriniz...")

    def tv_oyun(self):

        print("""****************************

        Sayı Tahmin Oyununa Hoşgeldiniz

        1 ile 100 arasında(1 ve 100 dahil) rastgele tahmin edin.
        ****************************""")
        tahmin_hakkı = 7
        rastgele_sayı = random.randint(1,100)

        while True:
            tahmin =  int(input("Tahmininiz:"))

            if (tahmin == rastgele_sayı):
                print("Sayı Sorgulanıyor....")
                time.sleep(1)
                print("Tebrikler!")
                print("Sayı",rastgele_sayı)
                break
            elif(tahmin < rastgele_sayı):
                print("Sayı Sorgulanıyor....")
                time.sleep(1)
                tahmin_hakkı -= 1
                print("Lütfen daha yüksek bir sayı söyleyin.")
                print("Tahmin Hakkı:",tahmin_hakkı)
            else:
                print("Sayı Sorgulanıyor....")
                time.sleep(1)
                tahmin_hakkı -= 1
                print("Lütfen daha düşük bir sayı söyleyin.")
                print("Tahmin Hakkı:",tahmin_hakkı)
            if (tahmin_hakkı == 0 ):
                print("Tahmin Hakkınız Bitti. Üzgünüz")
                print("Sayımız:",rastgele_sayı)
                break

    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):

        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda = Kumanda()


print("""
Televizyon Uygulaması
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanala Geçme
7. Televizyon Bilgileri
8. Hesap Makinasi
9. Sayi Bulma Oyunu
Çıkmak için 'q' ya basın.
""")

if (kumanda.tv_durum == "Kapalı"):
        print("TV KAPALI, Oncelikle TV'yi acmalisiniz...")

while True:

        işlem = input("İşlem listesi için 'p' ye basın. \nİşlemi Seçiniz: ")

        if (işlem == "p"):
            print("""
            Televizyon Uygulaması
            1. Tv Aç
            2. Tv Kapat
            3. Ses Ayarları
            4. Kanal Ekle
            5. Kanal Sayısını Öğrenme
            6. Rastgele Kanala Geçme
            7. Televizyon Bilgileri
            8. Hesap Makinasi
            9. Sayi Bulma Oyunu
            Çıkmak için 'q' ya basın.
            """)

        elif (işlem == "q"):
            print("Program Sonlandırılıyor...")
            break

        elif (işlem == "1"):
            kumanda.tv_ac()

        elif (işlem == "2"):
            kumanda.tv_kapat()

        elif (işlem == "3"):
            if (kumanda.tv_durum == "Kapalı"):
                print("TV KAPALI, Oncelikle TV'yi acmalisiniz...")
            else:
                kumanda.ses_ayarları()

        elif (işlem == "4"):
            if (kumanda.tv_durum == "Kapalı"):
                print("TV KAPALI, Oncelikle TV'yi acmalisiniz...")
            else:
                kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")
                kanal_listesi = kanal_isimleri.split(",")

                for eklenecekler in kanal_listesi:
                    kumanda.kanal_ekle(eklenecekler)

        elif (işlem == "5"):

            if (kumanda.tv_durum == "Kapalı"):
                print("TV KAPALI, Oncelikle TV'yi acmalisiniz...")

            else:
                print("Kanal Sayısı:",len(kumanda))

        elif (işlem == "6"):
            if (kumanda.tv_durum == "Kapalı"):
                print("TV KAPALI, Oncelikle TV'yi acmalisiniz...")

            else:
                kumanda.rastgele_kanal()

        elif (işlem == "7"):
            print(kumanda)

        elif (işlem == "8"):
            if (kumanda.tv_durum == "Kapalı"):
                print("TV KAPALI, Oncelikle TV'yi acmalisiniz...")
            else:
                kumanda.tv_cal()

        elif (işlem == "9"):
            if (kumanda.tv_durum == "Kapalı"):
                print("TV KAPALI, Oncelikle TV'yi acmalisiniz...")
            else:
                kumanda.tv_oyun()

        else:
            print("Geçersiz İşlem......")
