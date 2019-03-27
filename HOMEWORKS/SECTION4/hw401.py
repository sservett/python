import time

print("""=================================================
 
 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
 
 ================================================="""
)

boy = int(input("Boyunuzu giriniz: "))
kilo = int(input("Kilonuzu giriniz: "))

if boy > 3:
    boy = boy / 100

BKI = kilo / (boy ** 2)

print("Hesaplaniyor..")

time.sleep(1)

if BKI < 18.5:
    print("Zayifsiniz..")
elif BKI >= 18.5 and BKI < 25:
    print("Kilonuz idealdir..")
elif BKI >= 25 and BKI < 30:
    print("Sismansiniz maalesef..")
elif BKI >= 30:
    print("Uzgunum ama obezsiniz..")
else: 
    print("Lutfen gecerli bir deger giriniz..")