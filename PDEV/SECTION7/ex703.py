from math import *
from tkinter import *

def hesapla():
    veri = kutu.get()
    veri = str(veri)
    if veri == "":
        sonuc.config(text = "Lütfen boş bırakmayın.")
    else:
        isle = "global sonuc2;sonuc2 ="+veri
        exec(isle)
        print(isle,"\n",sonuc2)
        sonuc.config(text = str(sonuc2))

anapencere = Tk()
anapencere.geometry("800x600+100+100")
anapencere.title("Hesap Mak. V0.1 Beta")

sonuc = Label(anapencere)
sonuc.config(text = "Henüz işlem yapılmadı\n", font = "bold 18",fg = "blue")
sonuc.pack()

kutu = Entry(anapencere)
kutu.pack()

buton = Button(anapencere)
buton.config(text = "Hesapla!",command = hesapla)
buton.pack()

mainloop()
