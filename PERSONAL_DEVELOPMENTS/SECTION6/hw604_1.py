birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
yüzler=["","yüz","İkiyüz","Üçyüz","Dörtyüz","Beşyüz","Altıyüz","Yediyüz","Sekizyüz","Dokuzyüz"]
binler=["","Bin","İkibin","Üçbin","Dörtbin","Beşbin","Altıbin","Yedibin","Sekizbin","Dokuzbin"]

def okunus(sayı):
    birinci = sayı % 10
    ikinci = (sayı % 100) // 10
    üçüncü= (sayı % 1000) // 100
    dördüncü = sayı // 1000

    return binler[dördüncü] + " " +  yüzler[üçüncü] + " " +  onlar[ikinci] + " " + birler[birinci]


sayı =  int(input("Sayı:"))

print(okunus(sayı))