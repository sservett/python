from kutuphane import *

print("""***********************************

Kutuphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil

5. Baskı Yukselt

Çıkmak için 'q' ya basın. \n
***********************************""")

kutuphane = Kutuphane()

while True:
    işlem = input("\nYapacağınız İşlem:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor.....\n")
        print("Yine bekleriz....\n")
        break
    elif (işlem == "1"):
        print("\n")
        kutuphane.kitapları_goster()

    elif (işlem == "2"):
        isim = input("Hangi kitabı istiyorsunuz ? \n")
        print("Kitap Sorgulanıyor...\n")
        time.sleep(2)

        kutuphane.kitap_sorgula(isim)

    elif (işlem == "3"):
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tur = input("Tur: ")
        baskı = int(input("Baskı: "))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tur,baskı)

        print("Kitap ekleniyor....\n")
        time.sleep(2)

        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi....")


    elif (işlem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ?\n")

        cevap = input("Emin misiniz ? (E/H)\n")
        if (cevap == "E"):
            print("Kitap Siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi....")


    elif (işlem == "5"):
        isim = input("\nHangi kitabın baskısını yukseltmek istiyorsunuz ? : ")
        print("\nBaskı yukseltiliyor....\n")
        time.sleep(2)
        kutuphane.baskı_yukselt(isim)
        print("Baskı yukseltildi....")

    else:
        print("\nGeçersiz İşlem...\n")
