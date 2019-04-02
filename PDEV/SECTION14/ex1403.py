import time
        
def kareleri_hesapla(sayılar):
    sonuç = []
    baslama =  time.time()
    
    for i in sayılar:
        sonuç.append(i ** 2)
    print("Bu fonksiyon " + str(time.time() - baslama) + " saniye sürdü.")
    
def küpleri_hesapla(sayılar):
    sonuç = []
    baslama =  time.time()
    for i in sayılar:
        sonuç.append(i ** 3)
    print("Bu fonksiyon " + str(time.time() - baslama) + " saniye sürdü.")
 
    
 
print(kareleri_hesapla(range(100000)))
 
print(küpleri_hesapla(range(100000)))