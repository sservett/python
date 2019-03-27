"""
s =  "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans = dict()

for karakter in s:
    if (karakter in frekans):
        frekans[karakter] += 1
    else:
        frekans[karakter] = 1
for i,j in frekans.items():

    print(i,":",j)

#######################################################################

bas_harfler = ""

with open("siir.txt","r",encoding="utf-8") as file:
    for satır in file:
        if satır[0] == "K":
            bas_harfler += " "
        bas_harfler += satır[0]
print(bas_harfler+" ATATURK")


with open("mailler.txt","r",encoding="utf-8") as file:
    for satır in file:
        satır = satır[:-1]
        ext = (".com",".tr",".uk")
        if (satır.endswith(ext) and satır.find("@") != -1):
            print(satır)


"""

isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = list(zip(isim,soyisim))

liste.sort()

for i,j in liste:
    print(i,j)
